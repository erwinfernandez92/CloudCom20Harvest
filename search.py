import time
import datetime
from datetime import date, timedelta, datetime
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
        # earliestTweet = self.db.earliestId()
        # if earliestTweet != None:
        #     print("Fetching tweets before: " + earliestTweet)
        # Above logic is no longer needed as we have featched the last X
        # days twitter will give us, now we will just recursively run search
        # on the last 2 days data (and repeat) in order to catch up with
        # the stream API

        # iterate over results, see how many we can fetch
        max_id = None # earliestTweet
        count = 0
        while True:
            time.sleep(5)
            try:
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
                if len(results) == 0 or olderThanNDays(result.created_at, 2):
                    print("gracefully restarting to fetching latest")
                    max_id = None
                    count = 0
                    continue
            except Exception as e:
                print('error running search, trying again in 5 seconds')
                print(str(e))
                pass

# utility method
def olderThanNDays(dateObj, nDays):
    todayMinusN = datetime.utcnow() - timedelta(days=nDays)
    return (dateObj < todayMinusN)
