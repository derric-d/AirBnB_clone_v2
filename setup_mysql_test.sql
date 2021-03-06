-- MySQL TEST Setup Script
-- Create DB
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Give user all permissions on made db
GRANT ALL ON hbnb_test_db.*
TO 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
-- give dev user select
GRANT SELECT ON performance_schema.*
TO 'hbnb_test'@'localhost';
