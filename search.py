import time
from threading import Thread

class Searcher(Thread):
    def __init__(self, api, db, geo):
        Thread.__init__(self)
        self.api = api
        self.db = db
        self.geo = geo

    def run(self):
        # first get the lowest tweet, we assume we need to fetch more tweets
        # before this tweet
        earliestTweet = self.db.earliestId()
        if earliestTweet != None:
            print("Fetching tweets before: " + earliestTweet)

        # iterate over results, see how many we can fetch
        max_id = earliestTweet
        count = 0
        while True:
            time.sleep(4)
            results = self.api.search(geocode=self.geo, count=100, result_type="recent", max_id=max_id)
            bulk_tweets = []

            for result in results:
                # print(result.text)
                # print(result.created_at)
                if result.coordinates:
                    print(str(result.id) + str(result.coordinates))
                bulk_tweets.append(result._json)
                max_id = result.id

            # bulk insert all the tweets
            self.db.bulkInsert(bulk_tweets)

            count += len(results)
            print(result.created_at)
            print(count)
            if len(results) == 0:
                print("gracefully finishing")
                break
