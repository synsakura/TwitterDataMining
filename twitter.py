import tweepy
import sys

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)


consumer_key = 'YYJsnJa5MFl1CsfzEaP86kNeQ'
consumer_secret = 'jJ0J18VoHKuYQvBr136VD4bTkkLPKHSXNGpo6wngngezz83lQU'
access_token = '575460182-HMbmmYAUUUvWeZTkaFDU7aRRRQUjvQo1Fb3PROqI'
access_secret = 'ZgQoLHipKjkYq46IngULVUO06pkWEWwVxpYWRu5Wiupms'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

if (not api):
    print("Authentication Failed!")
    sys.exit(-1)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth= api.auth, listener=myStreamListener)
myStream.filter(track=['news'])