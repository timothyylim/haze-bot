#!/usr/bin/env python

#import scraping function 
import scrape_function 
import get_status

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

is_first_tweet = get_status.is_first(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)


updated_old = False

x = 0 
while x == 0:
	
	api_reading = scrape_function.test_function()



	if api_reading != "empty result" and is_new(api_reading) == True:
		updated_old = False
		if int(api_reading) >= 50 and int(api_reading) <= 100:
			print "----------------------------------"
			print api_reading + "Printing first tweet"
			message = "API: " + api_reading + " (PJ, Selangor). Pollution levels moderate."
			api.update_status(status = message)
			print datetime.now(malaysia_time)
			print "Sleeping for 20 minutes"
			print "----------------------------------"
			time.sleep(1200)

		elif int(api_reading) > 100 and int(api_reading) <= 200:
			print "----------------------------------"
			print api_reading + "Printing first tweet"
			message = "API: " + api_reading + " (PJ, Selangor). Pollution levels unhealthy."
			api.update_status(status = message)
			print datetime.now(malaysia_time)
			print "Sleeping for 20 minutes"
			print "----------------------------------"
			time.sleep(1200)

		elif int(api_reading) > 200 and int(api_reading) <= 300:
			print "----------------------------------"
			print api_reading + "Printing first tweet"
			message = "API: " + api_reading + " (PJ, Selangor). Pollution levels very unhealthy."
			api.update_status(status = message)
			print datetime.now(malaysia_time)
			print "Sleeping for 20 minutes"
			print "----------------------------------"
			time.sleep(1200)

		elif int(api_reading) > 300:
			print "----------------------------------"
			print api_reading + "Printing first tweet"
			message = "API: " + api_reading + " (PJ, Selangor). Pollution levels hazardous."
			api.update_status(status = message)
			print datetime.now(malaysia_time)
			print "Sleeping for 20 minutes"
			print "----------------------------------"
			time.sleep(1200)

	else:
		if api_reading == "empty result":

			if updated_old == False:
				updated_old = True
				api_reading = scrape_function.previous()
				# api_reading = get_status.return_last(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
				if int(api_reading) >= 50 and int(api_reading) <= 100:
					print "----------------------------------"
					print api_reading + "Printing first tweet"
					message = "API: " + api_reading + " (PJ, Selangor). Pollution levels moderate."
					api.update_status(status = message)
					print datetime.now(malaysia_time)
					print "Sleeping for 20 minutes"
					print "----------------------------------"
					time.sleep(1200)

				elif int(api_reading) > 100 and int(api_reading) <= 200:
					print "----------------------------------"
					print api_reading + "Printing first tweet"
					message = "API: " + api_reading + " (PJ, Selangor). Pollution levels unhealthy."
					api.update_status(status = message)
					print datetime.now(malaysia_time)
					print "Sleeping for 20 minutes"
					print "----------------------------------"
					time.sleep(1200)

				elif int(api_reading) > 200 and int(api_reading) <= 300:
					print "----------------------------------"
					print api_reading + "Printing first tweet"
					message = "API: " + api_reading + " (PJ, Selangor). Pollution levels very unhealthy."
					api.update_status(status = message)
					print datetime.now(malaysia_time)
					print "Sleeping for 20 minutes"
					print "----------------------------------"
					time.sleep(1200)

				elif int(api_reading) > 300:
					print "----------------------------------"
					print api_reading + "Printing first tweet"
					message = "API: " + api_reading + " (PJ, Selangor). Pollution levels hazardous."
					api.update_status(status = message)
					print datetime.now(malaysia_time)
					print "Sleeping for 20 minutes"
					print "----------------------------------"
					time.sleep(1200)

			

		else:
			print "----------------------------------"
			print "no results posted yet, sleeping for 10 minutes"
			print datetime.now(malaysia_time)
			time.sleep(600)




def is_new(api_reading):
	print "Printing last: "
	print get_status.return_last(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
	if api_reading != scrape_function.previous():
		return True
	else:
		return False 

