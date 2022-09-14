CREATE TABLE t_user (
  id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(20) NOT NULL,
  created_at TIMESTAMP without time zone NOT NULL DEFAULT now()
);

INSERT INTO t_user (name)
VALUES ('AAAAAA'),('BBBBBB'),('CCCCCC');