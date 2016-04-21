#!/usr/bin/python3
import base64
import tweepy
from streaming import Streamer
from search import Searcher

# constants for searching
melbourneRadial = "-37.814107,144.963280,100km"
melbourneBox = [143.7,-38.5,145.9,-37.05]

# just obfuscate, meaning these are harder to find / steal
firstHidden = base64.b64decode("VWxQNkdMc2s1TTJVVUEwVHVGZHVNREd2Yg==").decode("utf-8")
secondHidden = base64.b64decode("NHNqQ1VHWE81VGZqemM5RTNuUlFXUlVLTG1iY0M2dkFPS2p3d0tUZDYwbHFvVDNyZVM=").decode("utf-8")

thirdHidden = base64.b64decode("MjgwOTIyNTk0LXB4dTBtMnNqR01xeUU3ZTZhdmFOUUk0bmlDdXE2d2RoY202UmFRV04=").decode("utf-8")
fourthHidden = base64.b64decode("aVV4cVk3UjNCVE5lTWN6NmZRakloczJuYTRqbjV6RUx5cmtYdGdTYTFUNGs3").decode("utf-8")


# authenticate
auth = tweepy.OAuthHandler(firstHidden, secondHidden)
auth.set_access_token(thirdHidden, fourthHidden)
api = tweepy.API(auth)

# start searching for all tweets going back a week
# sf = Searcher(api)
# sf.fetch(melbourneRadial)

# start streaming tweets
listener = Streamer()
stream = tweepy.Stream(auth=api.auth, listener=listener)
stream.filter(locations=melbourneBox)
