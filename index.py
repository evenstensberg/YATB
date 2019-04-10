#!/usr/bin/python3

import tweepy
import os, sys, inspect
import sched, time
from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv('C_KEY'), os.getenv('C_KEY_S'))

auth.set_access_token(os.getenv('A_KEY'), os.getenv('A_KEY_S'))

api = tweepy.API(auth)


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
importDir = parentdir + "/spotify-api-benchmark"
sys.path.insert(0,importDir)

from bench import thank_you_next
s = sched.scheduler(time.time, time.sleep)
done = False

def poll_cb(sc):
    dat = api.user_timeline()
    for i in dat:
        t = getattr(i, 'text')
        if t == 'thank you, next spotify':
            song = thank_you_next(True)
            title = song['item']['external_urls']['spotify']
            text = "Howdy buckaroo 🤠\n playing: " + title
            api.update_status(text, getattr(i, 'id'))
            done = True
    print("Polling stuff...")
    if done is False:
        s.enter(5, 1, poll_cb, (sc,))

if done is False:
    s.enter(1, 1, poll_cb, (s,))
    s.run()