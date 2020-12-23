import tweepy
from tweepy import Stream
from tweepy import StreamListener
import json
from textblob import TextBlob
from datetime import datetime
import nltk
nltk.download('punkt')

import re
import csv

consumer_key = "mwQmK8teqcKDMsSIJETYwE8oc"
consumer_secret = "Maoqq3xubl8h9CzEIRyDjcH6E8Bo4GJUwuEqTONaCYFmExqmSb"
access_token = "1691282078-vkNt0V9aArk7FhAmPOebnmApivsmyBFMk90ob3r"
access_token_secret = "SQSfHyP9Gv4U1fYctz5YjK0YJGVePyleBVspAsniV2zpn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

header_name = ['tweet_sentiment', 'user_id', 'user', 'tweet', 'timestamp']
with open('sentiment2.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=header_name)
    writer.writeheader()

class listener(StreamListener):
    def on_data(self, data):
        raw_tweets = json.loads(data)
        try:
            tweets = raw_tweets['text']
            tweets = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/S+)"," ",tweets).split())
            tweets = ' '.join(re.sub('RT', ' ', tweets).split())
            blob = TextBlob(tweets.strip())

            dtime = raw_tweets['created_at']
            new_datetime = datetime.strftime(datetime.strptime(dtime,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
            print((new_datetime))

            user = raw_tweets['user']['screen_name']
            print(user)
            user_id = raw_tweets['user']['id']
            print(user_id)

            for sent in blob.sentences:
                tweet_sentiment = sent.sentiment.polarity
            
            with open('sentiment3.csv', 'a') as file:
                writer = csv.DictWriter(file, fieldnames=header_name)
                info = {
                    'tweet_sentiment': tweet_sentiment,
                    'user_id': user_id,
                    'user': user,
                    'tweet': tweets,
                    'timestamp': new_datetime
                }
                writer.writerow(info)
            print(tweets)
        except:
            print('Error')
            
    def on_error(self, status):
        print(status)

twitter_stream = Stream(auth, listener())
twitter_stream.filter(track = 'Padjadjaran')