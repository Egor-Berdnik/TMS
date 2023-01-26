-- fill users table
INSERT INTO users (name, age, gender, nationality)
VALUES
  ('Alex', 34, 'male', 'belarus'),
  ('Ann', 32, 'female', 'russia'),
  ('Kate', 25, 'male', 'germany');

-- fill posts table
INSERT INTO posts (title, description, user_id)
VALUES
  ('Alex 1st post', 'Hello! Im Alex, im 34 years old', 1),
  ('Alex 2nd post', 'My favourite programming language is Python!', 1),
  ('Ann 1st post', 'Hello! Im Ann, im 32 years old', 2),
  ('Ann 2nd post', 'My favourite programming language is Rust!', 2),
  ('Kate 1st post', 'Hello! Im Kate, im 25 years old', 3),
  ('Kate 2nd post', 'My favourite programming language is Java!', 3);

-- fill comments table
INSERT INTO comments (title, user_id, post_id)
VALUES
  ('Wow, its great!', 1, 2),
  ('Im 32 years old too!', 2, 3),
  ('I like Java too!', 3, 6);

-- fill likes table
INSERT INTO likes (user_id, post_id)
VALUES
  (1, 1),
  (1, 2),
  (1, 2),
  (2, 3),
  (2, 3),
  (3, 5),
  (3, 5),
  (3, 5);