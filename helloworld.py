#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'ADnmjCsRawtQgSErrM04r9R2T'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'is6oHYPGuFxpdtGopvwEAve7ZrOWt9OeYa7oeAoYwlXpESm5dp'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '2799884788-XmUHYzxuxmJGCPa5xQKH24z5gYfMUni9rNMeLM0'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'YwZagSUOCamgdkYLiLk5PIva4MauNwHFv2VKqc416HWhm'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(status = line)
    time.sleep(900)#Tweet every 15 minutes