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
DROP TABLE person;
-- create table
CREATE TABLE person (
    id int,
    name varchar(255),
    email varchar(255),
    contact_number varchar(255),
    PRIMARY KEY (id)
);

-- Truncate table
TRUNCATE TABLE person;

-- view table schema
DESCRIBE person;

-- Alter table
-- add new column
ALTER TABLE person ADD COLUMN dateofbirth date;
-- modify data type of column
ALTER TABLE person MODIFY dateofbirth year;
-- drop column
ALTER TABLE person DROP COLUMN dateofbirth;

-- constraints
-- NOT NULL, PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE, CREATE INDEX, DEFAULT
CREATE TABLE person (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL UNIQUE,
    contact_number varchar(255) DEFAULT NULL,
    PRIMARY KEY (id)
);

-- modify data type of column
ALTER TABLE person ADD COLUMN dateofbirth date;
-- modify constraint
ALTER TABLE person MODIFY dateofbirth year NOT NULL;
-- Remove unique constraint
ALTER TABLE person drop index email;

-- add primary key
ALTER TABLE person ADD PRIMARY KEY (ID);
-- drop primary key
ALTER TABLE Person DROP PRIMARY KEY;

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
ALTER TABLE orders DROP FOREIGN KEY FK_person_id;

-- add foreign key
ALTER TABLE orders ADD FOREIGN KEY (customer_id) REFERENCES person(id);

-- add foreign key with constraint name
ALTER TABLE orders ADD CONSTRAINT FK_person_id FOREIGN KEY (customer_id) REFERENCES person(id);

-- check constraint -> Age should be above 18
ALTER TABLE person ADD COLUMN age int NOT NULL CHECK (age>18);

-- Drop check constraint
ALTER TABLE person DROP CHECK person_chk_1;
-- Add Check constraint
ALTER TABLE person ADD CHECK (Age>=18);

-- change auto increment
ALTER TABLE person AUTO_INCREMENT=100;
```
