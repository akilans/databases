# ntroduction to Redis Data Structures  course from https://university.redislabs.com/

# Redis In memory data structure 

    * Redis is an open source (BSD licensed), NoSQL in-memory key-value data structure store, used as a database, cache and message broker.

    * High performance in memory store. Suitable for IoT, Ecommerce, FinTech etc.

    * Virtual lab url - https://8888-21087069.university.redislabs.com/entry.html

# WEEK 1

    * redis-cli - access redis cli [ default port 6379 ]
    * keys are the main part of redis to access, assign value. Unique, Binary safe
    * set name akilan
    * incr name - Fails , because it is string type
    * set age 30
    * incr age - returns 31
    * append name LS - returns "akilanLS"
    * hset friends akilan bangalore - Creating hash with value friends[ key:name value:location]
    * hset friends alex chennai
    * hset friends jegan kovai
    * hgetall friends
        1) "akilan"
        2) "bangalore"
        3) "jegan"
        4) "kovai"
        5) "alex"
        6) "chennai"

    * strings, hash, lists, sets, sorted sets are some basic data structure

# Basic Data Structure

    * set name akilan NX - Set name if name key not exists
    * set name akilan XX - Update name if name key exists
    * scan -0 match nam* - get key matchind with nam*
    * del name - delete key name
    * exists name - 1 if exists else 0
    * expire age 3000 - expires in seconds
    * pexpire age 3000 - expires in milliseconds
    * set age 31 PX|EX 3000 - Set and expire in single command
    * ttl age - Check the time to live
    * persists age - removes ttl
    * decrby age 2 - Decrement age by value 2
    * incrby age 2 - Increment age by value 2
    * When INCR/DECR redis encodes the value if it is an integer the perform the operation
    * type age - returns string 
    * object encoding age - returns integer
    * strlen age - returns the length of value asiigned to that key [ in this case 2]

# Hashes

    freinds{
        "akilan":{
            "name":"Akilan",
            "location":"Bangalore"
        },
        "alex":{
            "name":"Alex",
            "location":"Chennai"
        }
    }

    * hmset friends:akilan name Akilan location Bangalore
    * hmset friends:alex name Alex location Chennai 
    * hget friends:alex name - returns Alex
    * hkeys friends:alex - returns name, location
    * hvals friends:alex - returns Alex,Chennai
    * set name akilan
    * getrange name 0 2 - returns aki [ 0-2 ]


# WEEK 2