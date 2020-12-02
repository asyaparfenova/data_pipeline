from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json
import logging
import os
import pymongo
from decouple import config


# import authentifications credentioals from .env file
CONSUMER_API_KEY = config('CONSUMER_API_KEY')
CONSUMER_API_SECRET = config('CONSUMER_API_SECRET')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')
ACCESS_TOKEN = config('ACCESS_TOKEN')

def authenticate():
    """Function for handling Twitter Authentication."""
    auth = OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth

# connect to mongoDB
client = pymongo.MongoClient(host='mongodb', port=27017)
db = client.my_tweets
collection = db.new_berlin_tweets


# this class was copied from SPICED lesson with just a few modification from my side
class TwitterListener(StreamListener):

    def on_data(self, data):

        """Whatever we put in this method defines what is done with
        every single tweet as it is intercepted in real-time"""

        t = json.loads(data)

        tweet = {
        'text': t['text'],
        'username': t['user']['screen_name'],
        'followers_count': t['user']['followers_count']
        }
        
        collection.insert_one(tweet)
        


    def on_error(self, status):

        if status == 420:
            print(status)
            return False

if __name__ == '__main__':

    auth = authenticate()
    listener = TwitterListener()
    stream = Stream(auth, listener)
    stream.filter(track=['berlin'], languages=['en']) # we collecting tweets in English with mentioning of Berlin