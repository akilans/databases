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
    * 