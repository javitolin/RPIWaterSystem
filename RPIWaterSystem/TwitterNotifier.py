import tweepy
import os
import IOHelper

if not IOHelper.IsInRaspberry():
    from win10toast import ToastNotifier
    toaster = ToastNotifier()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
my_twitter_id = os.getenv("MY_TWITTER_ID")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

def SendTweet(message):
    if IOHelper.IsInRaspberry():
        api.send_direct_message(my_twitter_id, message)
    else:
        toaster.show_toast("RPIWaterSystem - Twitter", message)
