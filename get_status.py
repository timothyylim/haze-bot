
import tweepy, time, sys
from datetime import datetime
from pytz import timezone    

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'fjVIS7thOje3d1xYMYyJjMhKh'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'rhXMj52xqsl4x6RjL24Id4mjCWZlRtjon8Coo4pRSuquPn8XfC'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3691485079-bELhOycI3lX85cfDXjdjDO6Y5M0WWrxa0Rp4ZwT'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'krRjGLNm9Eydf2jWlsPamW6u3hqxX3sorTX2JNgbZCEuA'#keep the quotes, replace this with your access token secret


def is_first(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET):

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)


	malaysia_time = timezone('Asia/Kuala_Lumpur')
	current_hour = datetime.now(malaysia_time).strftime("%Y-%m-%d %H")
	# print "Current hour: " + current_hour
	
	tweets = []
	tweet_times = []
	for status in tweepy.Cursor(api.user_timeline,id="haze_watch").items(1):
		last_tweet = status.text

		print last_tweet
		tweets.append(last_tweet)
		time_last_tweet = status.created_at.strftime("%Y-%m-%d %H")
		tweet_times.append(time_last_tweet)

	print tweets
	print tweet_times
	# print "Last tweet: " + last_tweet
	# print "Time of last tweet: " + status.created_at.strftime("%Y-%m-%d %H")
	
	if current_hour == time_last_tweet[0]:

		return False

	else:
		return True 


def return_last(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET):
	print "Entering return last"
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	for status in tweepy.Cursor(api.user_timeline,id="haze_watch").items(1): 
			last_tweet = status.text
			time_last_tweet = status.created_at.strftime("%Y-%m-%d %H")

	print "Last tweet: " + last_tweet

	return last_tweet



# is_first(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
