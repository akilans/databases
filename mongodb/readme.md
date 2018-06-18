# Mongodb Basic cluster Admnistration Course - https://university.mongodb.com/

# Basic Commands :

    * mongod - Daemon to write data into a disk
    * mongo driver inteacts with mongod and doing CRUD operations
    * Default data path is /data/db
    * Default port is 27017
    * mongod --port 30000 --dbpath first_mongod --fork --logpath first_mongod/mongod.log
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