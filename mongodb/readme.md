# Mongodb Basic cluster Admnistration Course - https://university.mongodb.com/

mongo admin --host localhost:27000 --username m103-admin --password m103-pass


# Basic Commands :

    * mongod - Daemon to write data into a disk
    * mongo driver inteacts with mongod and doing CRUD operations
    * Default data path is /data/db
    * Default port is 27017
    * mongod --port 30000 --dbpath first_mongod --fork --logpath first_mongod/mongod.log - To run mongodb in background task
    * mongo --port 30000
    * use newDB - automatically creates DB but it will not show dbs. It will list only after it has any aollection
    * index is used to search document from collection fast
    * Documents are schemaless - can have different columns and data types
    * Documents can have maximum 16MB
    * Documents are stored in hard disk as BSON - Binary format converted back to JSON by mongodb driver
    * Mongodb config file - YAML file, [dppath, logpath, port, fork etc ] instead of passinig everything as a parameters can configure in a YAML file
    * Format of YAML config file is diffrent from command line parameter. Cleck the config.yaml file
    * mongod -f "config.yaml" or mongod --config "config.yaml"
    * mongo admin --host localhost:27000 --username m103-admin --password m103-pass - Connect to shell using user name & password
    * db.movies.renameCollection("new-movies") - rename collections
    * db.dropDatabase() - Drop DB
    * db.createCollection("movies")
    * db.getLogComponents() - get log levels [ -1 | 0 | 1-5 ]
    * db.adminCommand({"getLog":"global"}) - Prints all logs
    * db.getProfilingLevel() - 0 | 1 | 2
    * db.setProfilingLevel(1) - Change the default profilling level. Any query takes more than 100ms prints log. Creates system.profile collection to store profile information
    * db.setProfilingLevel(1,{slowms:0}) - now it will print log for every query
    * db.system.profile.find().pretty() - to see all the profiller logs
    * SCRAM - authentication mechanism [X.509 for community server ]
    * LDAP, Kerberos - Enterprise server
    * Built-in RBAC - 
    * db.createUser(
            { 
                user: "m103-application-user",
                pwd: "m103-application-pass",
                roles: [ { db: "applicationData", role: "readWrite" } ]
            }
        )
    * mongodump - Dumps binary json
    * mongorestore - Restores binary json
    * mongoexport - Exports json data
    * monfoimport - Imports json data
    * mongoimport --host localhost --port 27000 --username m103-admin --password m103-pass --db applicationData --collection products --authenticationDatabase admin /dataset/products.json

# Replication

    * Group of mongod
    * Multiple copies of data in different servers. Main server called primary & remaining nodes called secondary nodes
    * If failover happenes any one of secondary nodes will become primary by election
    * Read/write operation happens in primary node & remaining secondary nodes get sysnced automatically
    *  Binary based Replication - Primary & secondary nodes will be same OS & same version of mongodb. It is very fast & less data transfer
    * Statement based Replication - Based on Oplog, statement getting executed on secondary nodes. Primary & secondary node can be any OS fine
    * Limit of replica node is 50. max of 7 of these nodes participate in voting
    
    # Steps to configure replica set

        * Go to master machine & create key file using openssl and chmod 600
        * Edit config.yaml file add key file path under security. And also add replication settings [ Name ] in that config file
        * Start mongod with this config file [ Primary ]
        * Copy the key & config files to secondary nodes & start mongod
        * Login into primary node mongo shell & run rs.initiate().[ This needs admin user login to mongo shell ]
        * rs.status() - Check status of replica set
        * rs.add("SECONDARY_NODE1_HOST:MONGOD_PORT") | rs.add("SECONDARY_NODE2_HOST:MONGOD_PORT")
        * rs.isMaster() - Check which one is master and replication details
        * rs.stepDown() - Force the master to step down to check how secondary node becomes primary node
    
    # Replica set commands

        * rs.status() - Get information about replica set status
        * rs.isMaster() -  Shorter o/p [ members, which is primary and all ]
        * db.serverStatus()['repl'] - rbid [ whic is not there in rs.isMaster() command ]
        * rs.printReplicationInfo() - Oplog information
        
    # Oplogs

        * All the statements captured here
        * It has default size 5% of disk space. Once it full it starts to rewrite the statements. We can change the default size of this oplog 
    
    # Read & Write in Replica Set

        * Data created in primary replicated in secondaries
        * We can't read data in secondary directly but if we set rs.slaveOk() then we can read data. But we never write any data in secodary mongodb
        * If we shut down all the secondaries primary node becomes secondary so any application uses mongodb can't write any data

    # Failover & Election

        * Replica set must be odd number. For example 3,5,7 etc. In case of 4 node cluster if primary node stepdown 1 node vote for 1 node and another node for another node then it become tie. So again election will happen.It may repeat and not good for application
        * We can set the prioroty to zero of secondary node so that it will not become primary
    
    # Write Concern

        * Write concern level 0 - Don't wait for acknowlegement
        * Write concern level 1 - Default one. wait for acknowlegement from Primary
        * Write concern level >=2 - Wait for acknowlegement from primary & one or more secondary
        * Majority - If 3 node cluster 2, If 5 cluster node is 3. No need to hard code the level value
        * wtimeout - Mark as fail for particular timeout. Even the write is success within timeout duration then also it will mark it as failure
        * J{true|False} - node commit the write before sending the acknowlegement

    # Read Concern

        * Local - Default
        * Available - Sharded cluster
        * Majority - Stronger Gurantee
        * Linearizable - Good one
        * Instead of reading data from primary we can make the application to read data from secondary by mentioning readPredf parameter
        * Primary - Default
        * PrimaryPrefered
        * Secondary
        * SecondaryPrefered

# Sharding

    * Instead of keeping Documents in a single mongoDB server, it is distributed across mongodb instances. It is called shard cluster & horizontal scaling. Each distributed documents also stored in replicasets

    * Mongos is getting and responding to client requests.Meta data maintained [ where to look document in a shard cluster ]

    * Shard cluster is not recommended for all projects. If the project data more than 5TB and not able go for Vertical scaling then only we can go for Shard Cluster

    * Client -> MongoS -> Config Servers [ Meta data for all documents] -> Connect to correct shard [ which is replicated to avoid data loss ]

    # Steps to create shard cluster

        * Create 3 config server with replica sets -- Role will be config server
            * mongod -f csrs1.yaml 
            * mongod -f csrs2.yaml
            * mongod -f csrs3.yaml
        * Create Mongos process
            * mongos -f mongos.yaml
        * Create shard cluster with replica sets - Role will be shard cluster
            * mongod -f node1.yaml
            * mongod -f node2.yaml
            * mongod -f node3.yaml

    * config DB has all the information about how dbs, collections, chunks are distributed. chunks is the main one. We should not write any data in config db

    * Shard Keys -Immutable Indexed keys to distribute,query chunks of data
    * sh.enableSharding("DBNAME");
    * db.COLLECTION_NAME.createIndex({"COLLECTION_FIELD":1})
    * sh.shardCollection("DB_NAME.COLLECTION_NAME",{"COLLECTION_FIELD":1})
    * Shard possible for DB & Collection level
    * Shard DB can't automatically sharding the collections
    * We can have shard collection and unshard collection on the same db
    * Choose shard key in efficient way [ High cardinality, Low frequency, Low Monotonically changed ]

    * High cardinality - number of unique key values [ states of india - 30+ possible values. 30+ possible chunks . Days of week - 7 possible chunks, Boolean 2 possible chunks ]

    * Frequency - In case of states of india - If we are going to store most datas of tamilnadu, all the details goes to same chunks. It leads to performance issue.So repetation of each unique keys should be less

    * Monotonicaly - Timestamp is very unique but it keeps on increasing [ Range min max ]

    * When read, specify the index key so it ll be fast to get data. Otherwise it has to collect it from all shard clusters

    * Hashed Shard key - The underlying index key hashed and based on the hashed key the data is getting chunked & distributed on shard cluster. In case of timestamp it is very helpful but in other case the data now distributed all across the cluster. Querying the data takes time

    # Create Shard Key
        * sh.enableSharding("DB_NAME")
        * db.COLLECTION_NAME.createIndex( { "KEY_NAME" : 1 } )
        * sh.shardCollection("DB_NAME.COLLECTION_NAME", {"KEY_NAME" : 1 } )
        
    # Chunks

        * Default size is 64MB. We can change it. Based on shard key it get distributed across shard cluster
        
        * Config Chunks

            * use config
            * show collections
            * db.chunks.findOne()
            * db.settings.save({_id: "chunksize", value: 2})
            * sh.status()
            * db.chunks.find().pretty() - It lists chunks ranges [ We can see which ranges of chunks located on which shard]

    # Balancing 

        * balancer is responsible for even distribution of chunks on shard cluster

    * All queries from handled by mongos. If it finds the shard key then it will direct the request to shard cluster for that. Else it will collect the response from all the shard cluster and merge together & give it to client

    * db.products.find({"sku" : 1000000749 }).explain() - It explains how mongos is getting data. In this case sku is shard key. So it is a targetted query fetch data from a single shard

    * db.products.find( { "name" : "Gods And Heroes: Rome Rising - Windows [Digital Download]" } ).explain() - Find data from non index key scatter queries. It fetches data from all the shard clusters and merge it together

    # Configure & find it is a targetted query or Scattered Query

        * mongoimport --drop /dataset/products.json --port 26000 -u "m103-admin" \
-p "m103-pass" --authenticationDatabase "admin" \
--db m103 --collection products

        * use m103
        * show collections
        * db.products.createIndex({"sku":1})
        * db.adminCommand({shardCollection: "m103.products", key: {sku: 1}})
        * db.products.createIndex({"shippingWeight": 1})
        * 

