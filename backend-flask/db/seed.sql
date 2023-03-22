INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Brijesh Nambiar', 'brijeshnambiar@gmail.com', 'brijeshnambiar' ,'MOCK'),
  ('Anirudh Nambiar', 'anirudhnambiar@gmail.com', 'anirudhnambiar' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'brijeshnambiar' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )
