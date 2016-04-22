from tweepy.streaming import StreamListener
import json

class Streamer(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, db):
        self.db = db

    def on_data(self, data):
        jsonData = json.loads(data)
        self.db.insertTweet(jsonData)
        print(str(jsonData['id']) + " - " + str(jsonData['user']['screen_name']) + " - " + str(jsonData['coordinates']))
        if jsonData['coordinates'] != None:
            print(jsonData['text'])
            print(jsonData['created_at'])
        return True

    def on_error(self, status):
        print("error")
        print(status)
