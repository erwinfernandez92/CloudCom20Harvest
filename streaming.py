from tweepy.streaming import StreamListener
import json

class Streamer(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        jsonData = json.loads(data)
        print(jsonData['coordinates'])
        if jsonData['coordinates'] != None:
            print(jsonData['text'])
            print(jsonData['created_at'])
        return True

    def on_error(self, status):
        print("error")
        print(status)
