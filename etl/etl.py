import logging
import time
from sqlalchemy import create_engine
import pymongo
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from decouple import config

time.sleep(10)


def clean_tweet(tweet):
    '''clean tweet text from @usernames, RT, https...'''
    rt_regex = r"^RT "
    http_regex = r"http[^ ]*"
    user_regex = r"@[^ $\n]*"
    tweet = re.sub(rt_regex, '', tweet)
    tweet = re.sub(http_regex, '', tweet)
    tweet = re.sub(user_regex, '', tweet)
    return tweet


# connecting to mongodb
client = pymongo.MongoClient(host='mongodb', port=27017)
db = client.my_tweets
collection = db.new_berlin_tweets


# connecting to postgres
password = config('POSTGRES_PASSWORD', cast=int)
engine = create_engine(f'postgres://postgres:{password}@postgres:5432/postgres')


# creating psql-table if necessary
create_query = """
CREATE TABLE IF NOT EXISTS berlin_tweets(
    id VARCHAR(50) PRIMARY KEY,
    text VARCHAR(500),
    clean_text VARCHAR(500),
    username VARCHAR(100),
    followers_count INT,
    polarity_score FLOAT(8),
    status SMALLINT
);
"""
engine.execute(create_query)


# creating a vader sentiment analyzer
s = SentimentIntensityAnalyzer()


if __name__ == '__main__':
    while True:
        #reading tweets from mongodb, doing sentiment analysis and inserting tweets to PostgreSQL
        tweets = collection.find({})
        time.sleep(10)
        for tweet in tweets:
            if ('status' in tweet) == False or tweet['status'] == 0:
                tweet_text = tweet['text']
                tweet_text = clean_tweet(tweet_text)
                ps = s.polarity_scores(tweet_text)['compound']
                engine.execute('''INSERT INTO berlin_tweets(id,
                                                            text,
                                                            clean_text,
                                                            username,
                                                            followers_count,
                                                            polarity_score,
                                                            status)
                                  VALUES(%s, %s, %s, %s, %s, %s, %s)''',
                                  (f'''{tweet['_id']}''',
                                   f'''{tweet['text']}''',
                                   f'''{tweet_text}''',
                                   f"{tweet['username']}",
                                   tweet['followers_count'], ps, 1))
                collection.update_one({'_id': tweet['_id']}, {"$set": {"status":1}})
            else:
                None