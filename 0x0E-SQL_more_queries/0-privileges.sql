-- List all privileges of the MySQL users `user_0d_1` and `user_0d_2` on `localhost`
-- List user_0d_1 privileges
SHOW GRANTS IF EXISTS FOR "user_0d_1"@"localhost";
-- List user_0d_2 privileges
SHOW GRANTS FOR "user_0d_2"@"localhost";
