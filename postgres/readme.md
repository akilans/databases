# Postgres Notes

- [Full Course in Youtube](https://www.youtube.com/watch?v=qw--VYLpxG4)
- [Mock Data Generator](https://www.mockaroo.com/)

### Basic Commands

```
- psql - This is used to login into postgres
- \! clear -- clear console
- \l -- List dbs
- \q -- quit psql terminal
- help - \? -- Help and commnads lists

```

### Basic Queries

```sql
- CREATE DATABASE test;
- --\c test -- switch db
- DROP DATABASE test
- -- \c test -- switch db
- -- \dt --list tables
- CREATE TABLE person(
  id BIGSERIAL NOT NULL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  gender VARCHAR(7) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(50)
  );
- -- \d person -- describe table
- INSERT INTO person (first_name,last_name, gender,date_of_birth,email) values ('Akilan','Subramanian', 'MALE', date '1988-04-06', 'dummy@gmail.co');
- DROP TABLE person;
- DELETE FROM person where id=1;
```

### Import data and Filter data

```sql
- -- \i /vagrant/person.sql; Import data
- SELECT * FROM person ORDER BY id DESC;
- SELECT DISTINCT(country_of_birth) from person ORDER BY country_of_birth;
- select count(distinct(country_of_birth)) from person;
- SELECT * FROM person WHERE gender = 'Male' AND (country_of_birth = 'China' OR country_of_birth = 'India');
- SELECT * FROM person LIMIT 5 OFFSET 5;
- SELECT * FROM person where country_of_birth IN ('China','Thailand');
- SELECT * FROM person where date_of_birth BETWEEN '1988-01-01' AND '1989-01-01';
- SELECT * FROM person WHERE email LIKE '%google.%';
- SELECT * FROM person WHERE email LIKE '*___**@google.%';
- SELECT * FROM person WHERE country_of_birth ILIKE 'ch%' -- case insensitive
```

### Group by , Order by and Having

```sql
- SELECT country_of_birth,COUNT(*) AS no_of_people FROM person GROUP BY country_of_birth ORDER BY no_of_people DESC;
- SELECT country_of_birth,COUNT(*) AS no_of_people FROM person GROUP BY country_of_birth HAVING COUNT(*) > 100 ORDER BY no_of_people DESC;
```

### Min, Max, Avg

```sql
- select make,max(price) from car group by make;
- select make,min(price) from car group by make;
- select make,round(avg(price)) from car group by make;
- select id,make,model,price,(price * .10) as discount, (price - price * .10) as after_discount from car;
- select id, coalesce(email,'Email not provided') from person;
```

### Date

```sql
- select NOW() - interval '10 DAYS'; -- 2020-09-13 06:05:20.902815+00
- select (NOW() - interval '10 DAYS')::DATE; -- 2020-09-13
- select id,first_name,date_of_birth,age(now(),date_of_birth) from person;
```

### Primary key and Unique

```sql
- alter table person drop constraint person_pkey; -- remove primary
- alter table person add primary key(id); -- Add primary key
- alter table person add constraint unique_email unique(email); -- add unique columns
- alter table person add constraint unique_gender check(gender = 'Male' or gender='Female');
```

### Conflict, Upsert

```sql
- insert into person(id,first_name,last_name,email,gender,date_of_birth,country_of_birth) values(1,'Akilan','Subramanian','dummy@gmail.co','Male','1988-06-04','India') -- Throws duplicate id entry error
- insert into person(id,first_name,last_name,email,gender,date_of_birth,country_of_birth) values(1,'Akilan','Subramanian','dummy@gmail.co','Male','1988-06-04','India') ON CONFLICT(id) DO NOTHING; -- It will not throw error
- insert into person(id,first_name,last_name,email,gender,date_of_birth,country_of_birth) values(1,'Akilan','Subramanian','dummy@gmail.co','Male','1988-06-04','India') ON CONFLICT(id) DO UPDATE set email=EXCLUDED.email;
- insert into person(id,first_name,last_name,email,gender,date_of_birth,country_of_birth) values(1,'Akilan','Subramanian','dummy@gmail.co','Male','1988-06-04','India') ON CONFLICT(id) DO UPDATE set email=EXCLUDED.email, first_name=EXCLUDED.first_name,last_name=EXCLUDED.last_name,gender=EXCLUDED.gender,date_of_birth=EXCLUDED.date_of_birth,country_of_birth=EXCLUDED.country_of_birth;
```

### Join and Left Join

```sql
-- refer person-car.sql
- select person.first_name,person.country_of_birth,car.make,car.price from person join car on person.car_id=car.id;
- select person.first_name,person.country_of_birth,car.make,car.price from person left join car on person.car_id=car.id;
```

### Export CSV

```sql
- \copy (select * from person left join car on car.id=person.car_id) to '/vagrant/left-join-result.csv' delimiter ',' csv header;
```

### Bigserial Data type

```sql
- -- \d person - bigserial data type
- select * from person_id_seq;
- select nextval('person_id_seq'::regclass) -- autoincrement
- alter sequence person_id_seq restart with 11; -- reset sequence
```

### Extension

```sql
-- refer person-car-uuid.sql
- select * from pg_available_extensions;
- -- \df - list of functions
- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
- -- \df --
- select uuid_generate_v4();
- -- \i /vagrant/person-car-uuid.sql; Import data
```
