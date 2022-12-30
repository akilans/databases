# MYSQL notes

### MySQL Database Commands

```sql
-- list all the dbs
SHOW DATABASES;
--create db
DATABASE test;
-- drop db
DROP DATABASE test;
-- ctl + l -> to clear console

-- list tables
SHOW TABLES;

-- drop table
DROP TABLE persons;
-- create table
CREATE TABLE persons (
    id int,
    name varchar(255),
    email varchar(255),
    age int,
    contact_number varchar(255),
    PRIMARY KEY (id)
);

-- Truncate table
TRUNCATE TABLE persons;

-- view table schema
DESCRIBE persons;

-- Alter table
-- add new column
ALTER TABLE persons ADD COLUMN dateofbirth date;
-- modify data type of column
ALTER TABLE persons MODIFY dateofbirth year;
-- drop column
ALTER TABLE persons DROP COLUMN dateofbirth;

-- constraints
-- NOT NULL, PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE, CREATE INDEX, DEFAULT
CREATE TABLE persons (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL UNIQUE,
    age int NOT NULL,
    contact_number varchar(255) DEFAULT NULL,
    PRIMARY KEY (id)
);

-- modify data type of column
ALTER TABLE persons ADD COLUMN dateofbirth date;
-- modify constraint
ALTER TABLE persons MODIFY dateofbirth year NOT NULL;
-- Remove unique constraint
ALTER TABLE persons drop index email;

-- add primary key
ALTER TABLE persons ADD PRIMARY KEY (ID);
-- drop primary key
ALTER TABLE Persons DROP PRIMARY KEY;

-- create table with foreign key constrait
CREATE TABLE orders (
    id int NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    customer_id int NOT NULL,
    PRIMARY KEY (id)
);

-- To find constraints name
SHOW CREATE TABLE orders;

-- drop foreign key constraint
ALTER TABLE orders DROP FOREIGN KEY FK_persons_id;

-- add foreign key
ALTER TABLE orders ADD FOREIGN KEY (customer_id) REFERENCES persons(id);

-- add foreign key with constraint name
ALTER TABLE orders ADD CONSTRAINT FK_persons_id FOREIGN KEY (customer_id) REFERENCES persons(id);

-- check constraint -> Age should be above 18
ALTER TABLE persons ADD COLUMN age int NOT NULL CHECK (age>18);

-- Drop check constraint
ALTER TABLE persons DROP CHECK persons_chk_1;
-- Add Check constraint
ALTER TABLE persons ADD CHECK (Age>=18);

-- change auto increment
ALTER TABLE persons AUTO_INCREMENT=100;

-- change table name
ALTER TABLE person RENAME persons;
```

### SQL queries

```sql
-- select from table
SELECT * from persons

-- select specific columns from the table
SELECT name,email from persons;

-- Insert into table
INSERT INTO persons(name,email) VALUES("Akilan","akil.dove@gmail.com")

-- Select distinct values from table
SELECT DISTINCT(name) from persons;

-- Ignore duplicate values
SELECT count(DISTINCT(name)) from persons;

-- name the disctinct count
SELECT count(DISTINCT(name)) as TOTAL_USER from persons;

-- where condition ( =. >, <, >=, <=, IN, BETWEEN, NOT IN, LIKE)
SELECT * FROM persons where name = "Akilan";
SELECT * FROM persons where age > 18; -- <, >=, <=, != applies same
SELECT * FROM persons where age IN(10,15,20) -- select persons with age 10,15,20
SELECT * FROM persons where age NOT IN(10,15,20) -- select persons excluding age 10,15,20
SELECT * FROM persons where age BETWEEN 10 and 15 -- select persons with age between 10 to 15
SELECT * from persons WHERE name LIKE "%Aki%"; -- select persons name contains Aki
SELECT * from persons WHERE name LIKE "Aki%"; -- select persons name starts Aki

-- AND, OR, NOT examples
SELECT * from persons WHERE age > 18 AND age <=25; -- select all the persons age > 18 and <=25
SELECT * from persons WHERE NOT name = "Akilan"; -- except akilan select all the persons

-- ORDER BY
SELECT * FROM persons ORDER BY age;
SELECT * FROM persons ORDER BY age DESC;

-- Insert data
INSERT INTO persons(name,email,age) VALUES("Iniya","iniya@gmail.com",3);
INSERT INTO persons(name,email,age) VALUES("Akilan","akilan.468@gmail.com",34);
INSERT INTO persons(name,email,age) VALUES("Akilan","akil.dove@gmail.com",34);
```
