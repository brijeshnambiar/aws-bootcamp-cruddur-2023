SELECT pg_terminate_backend(pid)
FROM    pg_state_activity
WHERE 
pid <> pg_backend_pid()
AND datname = 'cruddur';
