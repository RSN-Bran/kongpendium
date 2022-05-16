import tweepy
import random
from kongbot import randomKong

import os
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_KEY_SECRET"))
auth.set_access_token(os.getenv("TWITTER_TOKEN"), os.getenv("TWITTER_TOKEN_SECRET"))
api = tweepy.API(auth)

try:
    randomKong()
    api.update_status("hey")
    print("Authentication Successful")
except Exception as e:
    print(e)