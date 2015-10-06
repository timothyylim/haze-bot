#!/usr/bin/env python

#import scraping function 
import scrape_function 
import get_status

# -*- coding: utf-8 -*-
 
import tweepy, time, sys

# Scraping packages
import requests
from bs4 import BeautifulSoup



import time
from pytz import timezone    

from datetime import datetime, timedelta

#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'fjVIS7thOje3d1xYMYyJjMhKh'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'rhXMj52xqsl4x6RjL24Id4mjCWZlRtjon8Coo4pRSuquPn8XfC'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3691485079-bELhOycI3lX85cfDXjdjDO6Y5M0WWrxa0Rp4ZwT'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'krRjGLNm9Eydf2jWlsPamW6u3hqxX3sorTX2JNgbZCEuA'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


time_curr = datetime.now(timezone('Asia/Kuala_Lumpur'))


def is_new(api_reading, time):

	print "Checking if tweet is new"
	if api_reading != scrape_function.previous(time_curr):
		print "Tweet is new"
		return True
	else:
		print "Tweet is old"
		return False 

def get_last_hour(time):
	last_hour = time_curr - timedelta(hours = 1)
	return last_hour

def update_twitter(api_reading):
	
	"Attempting to update Twitter"

	if int(api_reading) >= 50 and int(api_reading) <= 100:
		print "----------------------------------"
		print api_reading + "Printing first tweet"
		message = "API: " + api_reading + " (PJ, Selangor). Pollution levels moderate."
		api.update_status(status = message)
		print time_curr
		print "Sleeping for 20 minutes"
		print "----------------------------------"
		time.sleep(1200)

	elif int(api_reading) > 100 and int(api_reading) <= 200:
		print "----------------------------------"
		print api_reading + "Printing first tweet"
		message = "API: " + api_reading + " (PJ, Selangor). Pollution levels unhealthy."
		api.update_status(status = message)
		print time_curr
		print "Sleeping for 20 minutes"
		print "----------------------------------"
		time.sleep(1200)

	elif int(api_reading) > 200 and int(api_reading) <= 300:
		print "----------------------------------"
		print api_reading + "Printing first tweet"
		message = "API: " + api_reading + " (PJ, Selangor). Pollution levels very unhealthy."
		api.update_status(status = message)
		print time_curr
		print "Sleeping for 20 minutes"
		print "----------------------------------"
		time.sleep(1200)

	elif int(api_reading) > 300:
		print "----------------------------------"
		print api_reading + "Printing first tweet"
		message = "API: " + api_reading + " (PJ, Selangor). Pollution levels hazardous."
		api.update_status(status = message)
		print time_curr
		print "Sleeping for 20 minutes"
		print "----------------------------------"
		time.sleep(1200)

	else:
		print "BROKEN--------"
		 



x = 0 
while x == 0:

	time_curr = datetime.now(timezone('Asia/Kuala_Lumpur'))
	
	api_reading = scrape_function.scrape_website(time_curr)
	

	if api_reading == "empty result":
		print "result is empty"
		last_hour = get_last_hour(time_curr)
		api_reading = scrape_function.scrape_website(last_hour)
		
		if is_new(api_reading, last_hour):
			"Attempting to access update method"
			update_twitter(api_reading)

		else:
			"Old tweet has been tweeted, sleeping for 10 minutes"
			print time_curr 
			time.sleep(600)


	else:

		print "Need to update twitter"

		if is_new(api_reading, time_curr):
			update_twitter(api_reading)


		else:
			print "Tweet is already updated, sleeping for 10 minutes"
			print time_curr
			time.sleep(600)
		








