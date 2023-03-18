from psycopg_pool import ConnectionPool
import os

class DB:
  def __init__(self):
    self.init_pool()

  def init_pool(self):
    connection_pool = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_pool)

  def query_commit_returning_id(self,sql,*kwargs):
    print("SQL Statement - [commit with returning id]...")
    print(sql + "\n")
    try:
      conn = self.pool.connection()
      cur = conn.cursor()
      cur.execute(sql,kwargs)
      returning_id = cur.fetchone()[0]
      conn.commit()
      return returning_id
    except Exception as err:
      print_sql_err(err)
      #conn.rollback()

  def query_commit(self, sql):
    try:
      conn = self.pool.connection()
      cur = conn.cursor()
      cur.execute(sql)
      conn.commit()
    except Exception as err:
      print_sql_err(err)
      #conn.rollback()

  def query_array_json(self,sql):
    print("SQL Statement - [array]...")
    print(sql + "\n")
    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
        return json[0]

  def query_object_json(self, sql):
    print("SQL Statement - [object]...")
    print(sql + "\n")
    wrapped_sql = self.query_wrap_object(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
        return json[0]
  

  def query_wrap_object(self,template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {template}
    ) object_row);
    """
    return sql

  def query_wrap_array(self,template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql

  def print_sql_err(self,err):
    err_type, err_obj, traceback = sys.exc_info()
    line_num = traceback.tb_lineno

    print("\n psycopg ERROR", err, "on line number:", line_num)
    print("psycopg traceback:", traceback, "-- type:", err_type)

    print("\nextensions.Diagnostics:", err.diag)

    print("pgerrors:", err.pgerror)
    print("pgcode:", err.pgcode, "\n")


db = DB()