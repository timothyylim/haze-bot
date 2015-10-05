

import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from pytz import timezone    

#To strip non-numeric characters
import re


def test_function():

	print "Scrape function running"
	# Check the we are on the right page for the hour 
	right_page = False 

	malaysia_time = timezone('Asia/Kuala_Lumpur')
	current_hour = str(datetime.now(malaysia_time).hour)

	print "current hour: "
	print current_hour
	print "------------------"
	d = datetime.strptime(current_hour, "%H")
	d = d.strftime("%I:%M%p")
	target_time = str(d)

	# print "this is target time:"
	# print target_time

	# Navigate to the correct URL

	starting_url = "http://apims.doe.gov.my/v2/"
	hour_url = ""
	date_url = ""

	###############
	# set the hour URL
	###############
	current_hour_int = int(current_hour)


	if current_hour_int > 0 and current_hour_int < 6:
		hour_url = "hour1_"

	elif current_hour_int > 5 and current_hour_int <12:
		hour_url = "hour2_"

	elif current_hour_int > 11 and current_hour_int < 18:
		hour_url = "hour3_"

	elif current_hour_int > 17:
		hour_url = "hour4_"

	else:
		print "ERROR: could not get current hour"

	###############
	# set the date URL
	###############
	malaysia_time = datetime.now(malaysia_time)
	malaysia_date_url = str(malaysia_time.strftime('%Y-%m-%d')) + ".html"
	date_url = malaysia_date_url

	###############
	# put it all together 
	###############

	final_url = starting_url+hour_url+date_url
	# print "------------------"
	# print "this is the url"
	# print final_url
	# print "------------------"



	r = requests.get(final_url)
	soup = BeautifulSoup(r.content)
	pretty_soup = soup.prettify()


	tables = soup.findChildren('table')

	my_table = tables[0]

	rows = my_table.findChildren(['th', 'tr'])

	result = []

	for row in rows:
		cells = row.findChildren('td')

		result.append([])

		for cell in cells:

			if cell.string == None:
				output = str(cell.next)
				redone_output = concat_to_digit(output)
				result[-1].append(redone_output)
				# print redone_output

			else:

				value = cell.string
				value = value.encode('ascii', 'ignore').decode('ascii')
				string_value = str(value)
				result[-1].append(string_value)

	
	# print "----------------"
	# print "Result table"
	# print result[0]

	# print "Target time: "
	# print target_time

	# print "----------------"
	index = 0
	
	for row in result:
		if target_time in row:
			index = row.index(target_time)

			break 


	# Find PJ's index (44)
	# for row in result:
	# 	if 'Nilai' in row:
	# 		print "Nilai"
	# 		print result.index(row) 	
	# 		break 

	# print "----------------"
	# print "index: "
	# print index 
	# print "----------------"
	# print result[12]
	api_reading = result[44][index]
	# print "----------------"
	# print "raw API reading: "
	# print api_reading
	# print "----------------"

	if 	api_reading == "" or \
		api_reading == "n/a":

		print "empty result"
		return "empty result"

	else:
		if 	api_reading.endswith('*') or \
			api_reading.endswith('a') or \
			api_reading.endswith('b') or \
			api_reading.endswith('c') or \
			api_reading.endswith('&'):
			reading_length = len(api_reading)
			
			api_reading = api_reading[:reading_length-1]
			print "current API reading: "
			print api_reading
			print "Scrape DONE"
			return api_reading

		else:
			print "current API reading: "
			print api_reading
			print "Scrape DONE"
			return api_reading


def previous():

	print "Previous function running"
	# Check the we are on the right page for the hour 
	right_page = False 

	malaysia_time = timezone('Asia/Kuala_Lumpur')
	current_date = datetime.now(malaysia_time)
	yesterday = datetime.now(malaysia_time) - timedelta(days=1)
	print yesterday
	current_hour = current_date.hour
	
	if current_hour == 0:
		current_hour = 11
		current_date = yesterday

	else:
		current_hour = current_hour -1
	

	current_hour = str(current_hour)
	print "current hour: "
	print current_hour
	print "------------------"
	d = datetime.strptime(current_hour, "%H")
	d = d.strftime("%I:%M%p")
	target_time = str(d)

	print "this is target time:"
	print target_time

	# Navigate to the correct URL

	starting_url = "http://apims.doe.gov.my/v2/"
	hour_url = ""
	date_url = ""

	###############
	# set the hour URL
	###############
	current_hour_int = int(current_hour)
	# current_hour_int = 5

	print "CCC"
	print current_hour_int
	if current_hour_int >= 0 and current_hour_int <= 5:

		hour_url = "hour1_"

	elif current_hour_int > 5 and current_hour_int <= 11:
		hour_url = "hour2_"

	elif current_hour_int > 11 and current_hour_int <= 17:
		hour_url = "hour3_"

	elif current_hour_int > 17:
		hour_url = "hour4_"

	else:
		print "ERROR: could not get current hour"

	###############
	# set the date URL
	###############
	malaysia_time = current_date
	malaysia_date_url = str(malaysia_time.strftime('%Y-%m-%d')) + ".html"
	date_url = malaysia_date_url

	###############
	# put it all together 
	###############

	final_url = starting_url+hour_url+date_url
	print "------------------"
	print "this is the url"
	print final_url
	print "------------------"



	r = requests.get(final_url)
	soup = BeautifulSoup(r.content)
	pretty_soup = soup.prettify()


	tables = soup.findChildren('table')

	my_table = tables[0]

	rows = my_table.findChildren(['th', 'tr'])

	result = []

	for row in rows:
		cells = row.findChildren('td')

		result.append([])

		for cell in cells:

			if cell.string == None:
				output = str(cell.next)
				print "Before concat: " + output
				redone_output = concat_to_digit(output)
				result[-1].append(redone_output)

				print redone_output

			else:

				value = cell.string
				value = value.encode('ascii', 'ignore').decode('ascii')
				string_value = str(value)
				# print "before concat:" + string_value
				result[-1].append(string_value)

	
	print "----------------"
	print "Result table"
	print result[0]

	print "Target time: "
	print target_time

	print "----------------"
	index = 0
	
	for row in result:
		if target_time in row:
			index = row.index(target_time)

			break 


	# Find PJ's index (44)
	# for row in result:
	# 	if 'Nilai' in row:
	# 		print "Nilai"
	# 		print result.index(row) 	
	# 		break 

	print "----------------"
	print "index: "
	print index 
	print "----------------"
	# print result[12]
	api_reading = result[44][index]
	print "----------------"
	print "raw API reading: "
	print api_reading
	print "----------------"

	if 	api_reading == "" or \
		api_reading == "n/a":

		print "empty result"
		return "empty result"

	else:
		if 	api_reading.endswith('*') or \
			api_reading.endswith('a') or \
			api_reading.endswith('b') or \
			api_reading.endswith('c') or \
			api_reading.endswith('&'):
			reading_length = len(api_reading)
			
			api_reading = api_reading[:reading_length-1]
			print "current API reading: "
			print api_reading
			return api_reading

		else:
			print "current API reading: "
			print api_reading
			return api_reading


			
# print test_function()
def concat_to_digit(string):
	concatenated = re.sub("[^0-9,:]", "", string)
	if "AM" in string:
		return concatenated + "AM"
	else:
		return concatenated + "PM" 


previous()

