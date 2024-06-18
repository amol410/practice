mysql --host=localhost --user=root -p
password: password
\c ----to clear input statement
mysqlworkbench will ask you password

opening postgresql now >> asking
server[localhost]: default
database[postgresql]:which database ?
port [5432]: default
username:
password:password

now coming to mysql >>
in search mysqlshell
shell.connect({host:'localhost', user:'amol'}) then
root@localhost: password

\sql ---need to change your language first 

remeber postgreSQL also have sql shell

lecture 11 module 03

vs code >> extension SQLTools >> now this is not all
> install drivers >> sqltools mysql & sqltootls postgressql
> will ask you connection queries
> following line to avoid strong security --
> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'

lecture 12 module 03
> create schema in mysqlworkbench
> 
lecture 003 module 04

we are working on telently app from here
db(schema) has 3 tables users|employers|conversations

lecture 005 module 04
CREATE DATABASE talently; #no whitespace in database please
`backticks not supported by postgres`

once you create database change database connection settings 

lecture 008 module 04
enum help you to store -- status 
char - space given in start
varchar - normal

lecture 011 module 04

CREATE TABLE users (
user_name VARCHAR(255)
image_path VARCHAR(200)
);

INSERT INTO users(user_name, image_path)
VALUES('DBmax', 'uploads/image/dog.jpg');

lecture 012 module 04
for reserved keywords
CREATE TABLE "talently" ----postgresql
CREATE TABLE `talently` ----mysql

lecture 015 module 04

mysql
current_status ENUM('v1', 'v2')

postgres
CREATE TYPE my_status AS ENUM('v1', ...)
current status my_status

CREATE TABLE users(
full_name VARCHAR(200),
yearly_salary INT,
current_status ENUM('employed', 'self-employed', 'unemployed')
);

-- will be considered as comment

CREATE TYPE employment_status AS ENUM('employed','self-employed','unemployed')

lecture 016 module 04

INSERT INTO users(full_name, yearly_salary, current_status

) VALUES('max Schwartz', 20000, 'self-employed');

Lecture 017 module 04

adding 0 is not actually an error - sql package problem 

INSERT INTO users(full_name, yearly_salary, current_status)
VALUES('namit',200000,'employed');

SELECT * FROM users; -- it selects all rowsandcolums from currenttable

Lecture 018 module 04

float approximate - parenthesis not compulsory
decimal exact

float(5,2)  --total 5digits and only 2digits after point
NUMERIC -- parenthesis mandatory


Lecture 024 module 04
DROP TABLE table_name;


lecture 025 module 04
ALTER TABLE users 
ALTER COLUMN yearly_revenue SET DATA TYPE FLOAT;---postgresql

ALTER TABLE users
MODIFY COLUMN yearly_revenue FLOAT(5,2);

Lecture 026 module 04
SELECT AVG(yearly_salary) FROM users; --both postgres & mysql

lecture 027 module 04
CREATE TABLE users(
full_name VARCHAR(255) NOT NULL
SALARY INT -------obviously if not null not given so can be null 
);

ALTER TABLE users
ALTER COLUMN full_name SET NOT NULL,
ALTER COLUMN current_status SET NOT NULL