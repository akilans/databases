# ntroduction to Redis Data Structures  course from https://university.redislabs.com/

# Redis In memory data structure 

    * Redis is an open source (BSD licensed), NoSQL in-memory key-value data structure store, used as a database, cache and message broker.

    * High performance in memory store. Suitable for IoT, Ecommerce, FinTech etc.

    * Virtual lab url - https://8888-21087069.university.redislabs.com/entry.html

# WEEK 1

        * redis-cli - access redis cli [ default port 6379 ]
        * keys are the main part of redis to access, assign value. Unique, Binary safe
        * keys * - list all the keys
        * set name akilan
        * incr name - Fails , because it is string type
        * set age 30
        * incr age - returns 31
        * del name - delete key name
        * append name LS - returns "akilanLS"
        * strings, hash, lists, sets, sorted sets are some basic data structure

    # Basic Data Structure

        * set name akilan NX - Set name if name key not exists
        * set name akilan XX - Update name if name key exists
        * scan -0 match nam* - get key matchind with nam*
        * exists name - 1 if exists else 0
        * expire age 3000 - expires in seconds
        * pexpire age 3000 - expires in milliseconds
        * set age 31 PX|EX 3000 - Set and expire in single command
        * setex age 10 31 - Another way to set expire
        * ttl age - Check the time to live
        * persists age - removes ttl
        * decrby age 2 - Decrement age by value 2
        * incrby age 2 - Increment age by value 2
        * When INCR/DECR redis encodes the value if it is an integer the perform the operation
        * type age - returns string 
        * object encoding age - returns integer
        * strlen age - returns the length of value asiigned to that key [ in this case 2]

    # Hashes

        friends{
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
        * hmget friends:alex name location - returns Alex, Chennai - specify which fields we need

        * set name akilan
        * getrange name 0 2 - returns aki [ 0-2 ]

        friends{
            "akilan":"Bangalore",
            "jegan":"Kovai",
            "alex":"Chennai"
        }

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
        


# WEEK 2

    # Collections Datatypes

        * Lists
        * Sets
        * Sorted sets

    # List [ left --------> right Left & Right Push logic ]

        * ordered collection of strings.Duplicates allowed     
        * lpush friends Akilan Alex Annachi Jegan Kumar - Akilan value will be in the last of this list
        * lrange friends 0 -1 - returns
            1) "Kumar"
            2) "Jegan"
            3) "Annachi"
            4) "Alex"
            5) "Akilan"
        * lpop friends - removes kumar from the list - Last inserted value
        * rpush friends kumar - Add kumar at last
        * rpop friends - removes Akilan [ first in the list]
        * llen friends - returns the length of the list
        * lindex friends 2 - Returns alex
        * lrange friends 0 -1 - returns all the values in the list
        * lpushx friends mathan - Push the value if the key exists
        * linsert friends BEFORE mathan selvan - 
            1) "selvan"
            2) "mathan"
            3) "Jegan"
            4) "Annachi"
            5) "Alex"
            6) "Akilan"
        * linsert friends AFTER mathan naveen
            1) "selvan"
            2) "mathan"
            3) "naveen"
            4) "Jegan"
            5) "Annachi"
            6) "Alex"
            7) "Akilan"

    # SETS - Unique values
        * UnOrdered collection of strings.Duplication is not allowed and not nested
        * sadd num 1 2 3 4,4 - Add in the set [ removes duplicates ]
        * smembers num - returns 1,2,3,4
        * sadd num 7 - adds 7 in the set
        * scard num - returns 5 [ total members in the set ]
        * sadd num1 10 8 7 1 4 
        * sdiff num num1 - returns 2,3 [ presents only in num set ]
        * sdiff num1 num - returns 8,10 [ presents only in num1 set ]
        * sdiffstore num2 num num1 - stores the diff set values in new set [num2 = 2,3]
        * sunion num1 num2 - joining 2 sets
        * sunionstore num3 num1 num2
        * srem num 1 2 - removes 1,2 value from num
        * spop num - removes random value in the set
        * sinter num2 num3 - returns common values in both the sets
        * sinterstore num5 num2 num3 - stores common values in both the sets to num5 set
        * smove num2 num1 5 - moves the value 5 from num2 to num1

    # Sorted Sets

        *  zadd friends 30 akilan 25 mathan 26 naveen 24 selvan - Added friends with age
        * zrange friends 0 -1 - returns
            1) "selvan"
            2) "mathan"
            3) "naveen"
            4) "akilan"
        * zcard friends - returns 4 count the sorted sets
        * zcount friends 10 25 - returns 2 [ mathan slevan below 26] 
        * ZREMRANGEBYRANK friends 0 0 - removes lowest one [ selvan ]
        * zrem friends ram - removes from the sorted list
        * zrank friends akilan - returns 3 [ last value ]
        * zrevrank friends akilan - reverse rank returns 0
        * zscore friends akilan - returns score value 30
        * zadd friends 30 alex - can have same score in the sorted set [ it will show the same rank]
        * zscorebyrank friends 28 30 - returns akilan & alex [ min age 28 & max age 30 ]
        * ZRANGEBYSCORE q-1 0 40 withscores

    # Performance Big O notation:

        * Each redis command has Big O notation. Check the document. It shows the time of execution. Needs to consider for perfomance issues

    # Capped Collections and Set operations

        * rpush friends Akilan Alex Annachi Jegan Kumar
        * lrange friends 0 -1
            1) "Akilan"
            2) "Alex"
            3) "Annachi"
            4) "Jegan"
            5) "Kumar"
        * ltrim friends 0 2 - Keep only top 3 friends
        * lrange friends 0 -1
            1) "Akilan"
            2) "Alex"
            3) "Annachi"


        * zadd movie:kathi 500 akilan 500 annachi 500 jegan
        * zadd movie:thupaki 500 akilan 500 annachi 500 alex
        * zinterstore totalspent 2 movie:kathi movie:thupaki aggregate sum
        * zrange totalspent 0 -1 withscores
            1) "akilan"
            2) "1000"
            3) "annachi"
            4) "1000"

    # Attribute Search

        * Object Inspection
        * Faceted search
        * Hashed Index

        # Object Inspection : 

            * It is traditional method. Get all the keys and loop through all the attributes and compare the value & return the value. It is not a efficient one. 

            * If we have freinds set [key - akilan,alex,kumar] and need to return the friends who is staying in bangalore. We need to loop through all the friends keys and filter the location

            * If we have more keys [more friends ] loop through all the keys consumes lot of time



        # Faceting :

            * Create another set with defined attributes in this case[friends.location].Intersect the the sets it returns the common values and filter the result

            * If we have more attributes to filter [ location,age,job] then need to create more set for comparison

        #  Hashed Index       

    # Transactions

        * Start with MULTI and enter the commands. It will be in the queue. EXEC is called to execute all the queued commands sequentially

        * If any syntax errors redis throws an error and stops executing transactions

        * DISCARD throws and clear all the queued commands

        * Nested transactions not supported

        * If suppose in the middle of modifying the key command is in the Queue and it got changed by external action redis tranaction executes the command. In case if you want to stop the action, then watch the key before starting transactions[MULTI]. It is called optimistic concurrency control

    # Object Storage

        * 

    # Inventory Control

        * This explains how bus ticket booking system works. Start transaction by blocking number of seats. If any failure / timeout happens rollback to original one. Else conform booking and reduce the seats

    # Bit Fields

        * BITFIELD akilan set u8 0 29 - Key is akilan, u8 - 8bit unsigned value. 0 is offset

        * BITFIELD akilan get u8 0 - Get tha value

        * TYPE akilan - returns as string

        * object encoding akilan - returns raw

        * BITFIELD akilan incrby u8 0 1 - Increment value by 1

        * get akilan - returns \x1e - hexadecimal value for 30

    # Bit Arrays

        * bitfield akilan set u8 #1 3

        * bitfield akilan1 set u8 #1 2

        * bitpos akilan 1 - returns 14 [ 00000000 00000011 ]  offset not #0 , here #1 [ 16 bit data - from position 14 , bit 1 starts ]

        * bitop or akilan2 akilan akilan1

        * bitcount akilan - returns 2 [ 00000011 ]

        * bitcount akilan1 - returns 1 [ 00000010 ]

        * bitcount akilan2 - returns 2 [ 03 - 00000011 ]


    # Publish & Subscribe

        * open 2 redis cli
        * subscribe my-channel - Waiting for the publisher to get a message
        * publish my-channel "Hello from terminal1" - Send message to all subscribers
        * psubscribe my-ch* - subscribe with wild card pattern
        * publish my-*  - publish with wild card pattern
        * pubsub channels * - list al the chananels
        * pubsub numsub ch-? ch-1 ch-2 - Returns number of subsribers for each channel
        * pubsub numpat - number of pattern subscribers
        
    # Geospatial

        * It is a sorted sets
        * geoadd tenkasi LAT LONG "Tenkasi Railway station"
        * geoadd tenkasi LAT LONG "Tenkasi Temple"
        * zrange tenkasi 0 -1 withscores
        * LAT & LONG get hashed by redis. 52 bits used to store hashed value
        * geopos tenkasi "Tenkasi Railway station" - returns LAT & LONG for the location
        * geohash tenkasi "Tenkasi Railway station" - returns hash value of location
        * geodist tenkasi "Tenkasi Railway station" "Tenkasi Temple" [m|ft|km|mi]- Returns  the distance between two places