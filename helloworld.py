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



# is_first_tweet = get_status.is_first(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)



def is_new(api_reading):
	if api_reading != scrape_function.previous():
		return True
	else:
		return False 



def get_last_hour(time):
	last_hour = time - timedelta(hours = 1)
	return last_hour

def update_twitter(api_reading):
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


x = 0 
while x == 0:

	time = datetime.now(timezone('Asia/Kuala_Lumpur'))
	
	api_reading = scrape_function.scrape_website(time)
	

	if api_reading == "empty result":
		last_hour = get_last_hour(time)
		api_reading = scrape_function.scrape_website(last_hour)
		
		if is_new(api_reading):
			update_twitter(api_reading)


	else:
		update_twitter(api_reading)


	


	# api_reading = scrape_function.scrape_website()



	# if api_reading != "empty result" and is_new(api_reading) == True:
	# 	updated_old = False
	# 	if int(api_reading) >= 50 and int(api_reading) <= 100:
	# 		print "----------------------------------"
	# 		print api_reading + "Printing first tweet"
	# 		message = "API: " + api_reading + " (PJ, Selangor). Pollution levels moderate."
	# 		api.update_status(status = message)
	# 		print datetime.now(malaysia_time)
	# 		print "Sleeping for 20 minutes"
	# 		print "----------------------------------"
	# 		time.sleep(1200)

	# 	elif int(api_reading) > 100 and int(api_reading) <= 200:
	# 		print "----------------------------------"
	# 		print api_reading + "Printing first tweet"
	# 		message = "API: " + api_reading + " (PJ, Selangor). Pollution levels unhealthy."
	# 		api.update_status(status = message)
	# 		print datetime.now(malaysia_time)
	# 		print "Sleeping for 20 minutes"
	# 		print "----------------------------------"
	# 		time.sleep(1200)

	# 	elif int(api_reading) > 200 and int(api_reading) <= 300:
	# 		print "----------------------------------"
	# 		print api_reading + "Printing first tweet"
	# 		message = "API: " + api_reading + " (PJ, Selangor). Pollution levels very unhealthy."
	# 		api.update_status(status = message)
	# 		print datetime.now(malaysia_time)
	# 		print "Sleeping for 20 minutes"
	# 		print "----------------------------------"
	# 		time.sleep(1200)

	# 	elif int(api_reading) > 300:
	# 		print "----------------------------------"
	# 		print api_reading + "Printing first tweet"
	# 		message = "API: " + api_reading + " (PJ, Selangor). Pollution levels hazardous."
	# 		api.update_status(status = message)
	# 		print datetime.now(malaysia_time)
	# 		print "Sleeping for 20 minutes"
	# 		print "----------------------------------"
	# 		time.sleep(1200)

	# else:
	# 	if api_reading == "empty result":

	# 		if updated_old == False:
	# 			updated_old = True
	# 			api_reading = scrape_function.previous()
	# 			# api_reading = get_status.return_last(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
	# 			if int(api_reading) >= 50 and int(api_reading) <= 100:
	# 				print "----------------------------------"
	# 				print api_reading + "Printing first tweet"
	# 				message = "API: " + api_reading + " (PJ, Selangor). Pollution levels moderate."
	# 				api.update_status(status = message)
	# 				print datetime.now(malaysia_time)
	# 				print "Sleeping for 20 minutes"
	# 				print "----------------------------------"
	# 				time.sleep(1200)

	# 			elif int(api_reading) > 100 and int(api_reading) <= 200:
	# 				print "----------------------------------"
	# 				print api_reading + "Printing first tweet"
	# 				message = "API: " + api_reading + " (PJ, Selangor). Pollution levels unhealthy."
	# 				api.update_status(status = message)
	# 				print datetime.now(malaysia_time)
	# 				print "Sleeping for 20 minutes"
	# 				print "----------------------------------"
	# 				time.sleep(1200)

	# 			elif int(api_reading) > 200 and int(api_reading) <= 300:
	# 				print "----------------------------------"
	# 				print api_reading + "Printing first tweet"
	# 				message = "API: " + api_reading + " (PJ, Selangor). Pollution levels very unhealthy."
	# 				api.update_status(status = message)
	# 				print datetime.now(malaysia_time)
	# 				print "Sleeping for 20 minutes"
	# 				print "----------------------------------"
	# 				time.sleep(1200)

	# 			elif int(api_reading) > 300:
	# 				print "----------------------------------"
	# 				print api_reading + "Printing first tweet"
	# 				message = "API: " + api_reading + " (PJ, Selangor). Pollution levels hazardous."
	# 				api.update_status(status = message)
	# 				print datetime.now(malaysia_time)
	# 				print "Sleeping for 20 minutes"
	# 				print "----------------------------------"
	# 				time.sleep(1200)

			

	# 	else:
	# 		print "----------------------------------"
	# 		print "no results posted yet, sleeping for 10 minutes"
	# 		print datetime.now(malaysia_time)
	# 		time.sleep(600)






