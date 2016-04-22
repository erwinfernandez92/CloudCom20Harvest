import couchdb

class DBInterface:
    def __init__(self, dbhost):
        self.couch = couchdb.Server(dbhost)
        self.rawDB = self.couch['raw_tweets']

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
