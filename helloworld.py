#!/usr/bin/env python

#import scraping function 
import scrape_function 

# -*- coding: utf-8 -*-
 
import tweepy, time, sys

# Scraping packages
import requests
from datetime import datetime
from pytz import timezone    
from bs4 import BeautifulSoup

# Get time now

malaysia_time = timezone('Asia/Kuala_Lumpur')
time_now = datetime.now(malaysia_time)

#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'fjVIS7thOje3d1xYMYyJjMhKh'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'rhXMj52xqsl4x6RjL24Id4mjCWZlRtjon8Coo4pRSuquPn8XfC'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3691485079-bELhOycI3lX85cfDXjdjDO6Y5M0WWrxa0Rp4ZwT'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'krRjGLNm9Eydf2jWlsPamW6u3hqxX3sorTX2JNgbZCEuA'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open('helloworld.txt')
f=filename.readlines()
filename.close()

# api_reading = scrape_function.test_function()

# set the seed reading
print "Enter Scrape function"
api_reading_seed = scrape_function.test_function()
print "----------------------------------"
print "api reading seed is "
print api_reading_seed
print "at " + str(time_now)
print "----------------------------------"

# print api_reading_seed

# api.update_status(status = "Hello World!")
x = 0 
count = 0
count_empty = 0
while x == 0:
	
	api_reading = scrape_function.test_function()

	if api_reading == "empty":
		print "----------------------------------"
		print api_reading + "empty, so going to sleep for 15 mins"
		# api.update_status(status = "empty so going to sleep for 1 min" + str(count_empty))
		count_empty += 1
		print time_now
		print "----------------------------------"
		time.sleep(900)
	elif api_reading != api_reading_seed:
		print "----------------------------------"
		api.update_status(status = api_reading)
		print "read updated, sleeping for 40 mins"
		print api_reading
		print datetime.now()
		print "----------------------------------"
		time.sleep(2400)
	else:
		print "----------------------------------"
		print "reading is the same, going to sleep"
		print "going to sleep for 15 min:" + str(count)
		# api.update_status(status = "going to sleep for 15 mins:" + str(count))
		count += 1 
		print datetime.now()
		print "----------------------------------"
		time.sleep(900)




# for line in f:
#     api.update_status(status = line)
#     time.sleep(60)#Tweet every 15 minutes