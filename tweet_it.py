#!/usr/bin/python3

import tweepy
import os, sys, inspect
from dotenv import load_dotenv
load_dotenv()

status = None

if len(sys.argv) > 1:
    status = sys.argv[1]
else:
    sys.exit()

    
auth = tweepy.OAuthHandler(os.getenv('C_KEY'), os.getenv('C_KEY_S'))

auth.set_access_token(os.getenv('A_KEY'), os.getenv('A_KEY_S'))

api = tweepy.API(auth)
api.update_status(status)