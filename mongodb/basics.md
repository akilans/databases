# MongoDB Basics Course - https://university.mongodb.com/

Concepts :

    * Open source document based NoSQL DB. 
    * DB has Collections. Collections has documents.Document is based on JSON.Document stores string, int, float, array & nested documents
    * Compass GUI based MongoDB client
    * sudo apt-get install -y mongodb-org
    * sudo service mongod start - start mongodb as a service
    * mongo - to access mongo shell
    * service --status-all
    * systemctl -l --type service --all - It will show all the runnind services [ find mongodb service ]

# CRUD operation:

    * show dbs - List all the DBs
    * use DB_NAME - Use database
    * show collections - List all the collections in the DB
    * db.my-collections.find() -> List all the documents in the collection
    * db.my-collections.find().pretty() -> List all the documents in the collection in readable format
    * db.movieNew.find({title:"kathi"}) - Find with condition
    * db.movieDetails.find({"awards.wins": 2, "awards.nominations": 2}).count() - Filter with objects and conditions
    * db.movieDetails.find({actors:{$in:["Seth MacFarlane", "Charlize Theron"]}}) - In array filter
    * db.movieDetails.find({actors:{$all:["Seth MacFarlane", "Charlize Theron"]}})
    * db.movieDetails.find({},{title:1}) - Returns only title column, _id will come by default but we can hide _id:0

    * db.users.insert({"name":"Alex","age":30,"company":"Ericsson"}) - Create collection if not exists and insert document

    * mongo "mongodb://cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/test?replicaSet=Cluster0-shard-0" --authenticationDatabase admin --ssl --username m001-student --password m001-mongodb-basics - Connect to atlas cluster. We mentioned 3 DB URL for high availablity & replica set

    * db.dropDatabase(); - Drop the current DB
    * load("backup.js") - Import DB into the mongo
    * load("/home/akilan/Downloads/loadMovieDetailsDataset.js") - Full path also works fine

    * db.users.insertOne({_id:"jk8y89b8y98y9","name":"Alex","age":30,"company":"Ericsson"}) - Create collection if not exists and insert document
    * db.movieNew.insertMany([{title:"kathi",year:2009},{title:"Thupakki",year:2010}],{ordered:false}); - If any error during insertion it will not stop {ordered: false}

    * db.movieNew.updateOne({title:"kathi"},{$set:{title:"Kaththi"}}) - Update only the first match
    * db.movieNew.update({title:"kathi"},{$set:{title:"Kaththi"}}) - Update all the matches - There are many options to update with conditions. check the documentation
    * db.movieNew.update({"title":"Theri"},{$set:{title:"Theri",year:"2017"}},{upsert:true}); - Update if filter returns row else insert it 
    * db.movieNew.replaceOne({"title":"Theri"},{title:"Theri New",year:"2017"}) - Replace the document with new one

    * db.movieNew.deleteOne({title:"kathi"}) - Delete first movie title kathi
    * db.movieNew.deletemany({title:"kathi"}) - Delete all movie title kathi

# Query Operator [ $eq,$lt, $gt,$gte,$lte,$nq,$in,$exists,$type,$or,$and,$not,$nor etc... ]

    * db.movieNew.find({year:{$gt:2000}} - Greater than
    * db.movieNew.find({year:{$lt:2000}} - Less than 
    * db.movieNew.find({actor:{$exists:true}}) - List the documents which has actor column
    * db.movieNew.find({year:{$type:"string"}}) - Filter the document column with type
    * db.movieNew.find({year:{$type:"number"}})
    * db.movieNew.find({$or:[{year:"2017"},{year:2015}]})
    * db.movieNew.find({$and:[{year:"2017"},{year:2015}]})
    * db.movieNew.find({title:{$regex:/^Ka*/}}) - Using regular expression to filter the document
    * 