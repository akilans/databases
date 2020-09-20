# Postgres

- psql
- \! clear - clear console
- \l -> List dbs
- \q -> quit psql terminal
- help - \? - Help and commnads lists
- CREATE DATABASE test;
- \c test - switch db
- DROP DATABASE test
- \c test
- \dt - list tables
- CREATE TABLE person(
  id BIGSERIAL NOT NULL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  gender VARCHAR(7) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(50)
  );
- INSERT INTO person (first_name,last_name, gender,date_of_birth,email) values ('Akilan','Subramanian', 'MALE', date '1988-04-06', 'akil.dove@gmail.com');
- DROP TABLE person;
- \i /vagrant/person.sql;
- SELECT \* FROM person ORDER BY id DESC;
- SELECT DISTINCT(country_of_birth) from person ORDER BY country_of_birth;
- SELECT \* FROM person WHERE gender = 'Male' AND (country_of_birth = 'China' OR country_of_birth = 'India');
- SELECT \* FROM person LIMIT 5 OFFSET 5;
- SELECT \* FROM person where country_of_birth IN ('China','Thailand');
- SELECT \* FROM person where date_of_birth BETWEEN '1988-01-01' AND '1989-01-01';
- SELECT \* FROM person WHERE email LIKE '%google.%';
- SELECT \* FROM person WHERE email LIKE '**\_\_\_**@google.%';
- SELECT \* FROM person WHERE country_of_birth ILIKE 'ch%' - case insensitive
- SELECT country_of_birth,COUNT(\*) AS no_of_people FROM person GROUP BY country_of_birth ORDER BY no_of_people DESC;
- SELECT country_of_birth,COUNT(\*) AS no_of_people FROM person GROUP BY country_of_birth HAVING COUNT(\*) > 100 ORDER BY no_of_people DESC;
