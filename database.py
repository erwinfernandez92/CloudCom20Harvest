from couchdb import design, Server

dbname = 'raw_tweets'

class DBInterface:
    def __init__(self, dbhost):
        self.couch = Server(dbhost)
        # setup the database incase it isn't already
        self.setupDB()
        # connect to the database
        self.rawDB = self.couch[dbname]

    def setupDB(self):
        try:
            # this command will throw an exception if the db already exists
            db = self.couch.create(dbname)
            mapFunc = 'function(doc) { emit(doc._id, doc._id); }'
            view = design.ViewDefinition('harvster', 'min', mapFunc)
            view.sync(db)
        except Exception as e:
            print('Error creating database (probably because it already exists)')
            print(str(e))
            pass

    def insertTweet(self, tweetDoc):
        tweetDoc['_id'] = tweetDoc['id_str']
        try:
            self.rawDB.save(tweetDoc)
        except couchdb.http.ResourceConflict:
            print("Update conflict: "  + tweetDoc['id_str'])
            pass

    def bulkInsert(self, tweetDocs):
        for doc in tweetDocs:
            doc['_id'] = doc['id_str']
        self.rawDB.update(tweetDocs)

    def findTweetID(self, id):
        viewResults = self.rawDB.view('harvester/tweetids', key=id)
        for result in viewResults:
            return result.id
        return None

    def earliestId(self):
        viewResults = self.rawDB.view('harvester/min')
        for result in viewResults:
            return result.id
        return None
