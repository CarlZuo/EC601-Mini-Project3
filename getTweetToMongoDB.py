from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient

# filter words
WORDS = ["Iphone", "Wechat", "Jay Chou"]

MONGO_HOST = 'mongodb://localhost:12050/twitter_database' 
FILE_NAME = "tweets_search_data.json" 

class StreamListener(tweepy.StreamListener):
    # This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # if connect the streamer will print something
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        # When receiving data from twitter will call this method
        try:
            print(data)

            with open(FILE_NAME, 'a') as tf:  # write data to file
                tf.write(data)

            client = MongoClient(MONGO_HOST)  # connect mongodb
            db = client.twitter_database  # create db
            data_json = json.loads(data)  # Decode the JSON from Twitter
            db.twitterdb_collection.insert(data_json)  # insert the data into the mongodb into a collection

        except Exception as e:
            print(e)


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)

# print("Searching keywords are: " + str(WORDS))  # filter keywords