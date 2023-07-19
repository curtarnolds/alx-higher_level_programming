-- Create the MySQL user `user_0d_1` if it doesn't exist
CREATE USER IF NOT EXISTS user_0d_1 IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL PRIVILEGES ON *.* TO "user_0d_1"@"localhost";
