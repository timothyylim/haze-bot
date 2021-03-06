

import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from pytz import timezone    

#To strip non-numeric characters
import re


def get_current_hour(time):
	current_hour = time.hour 
	return current_hour



def get_target_time(current_hour):
	# print "current hour: "
	# print current_hour
	# print "------------------"
	current_hour = str(current_hour)
	d = datetime.strptime(current_hour, "%H")
	d = d.strftime("%I:%M%p")
	target_time = str(d)
	return target_time


def generate_url(target_time, current_hour):

	# Navigate to the correct URL
	starting_url = "http://apims.doe.gov.my/v2/"
	hour_url = ""
	date_url = ""
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
	malaysia_time = datetime.now(timezone('Asia/Kuala_Lumpur'))
	malaysia_date_url = str(malaysia_time.strftime('%Y-%m-%d')) + ".html"
	date_url = malaysia_date_url

	###############
	# put it all together 
	###############

	final_url = starting_url+hour_url+date_url

	return final_url



def scrape_website(time):

	print "Scrape function running"


	current_hour = get_current_hour(time)
	target_time = get_target_time(current_hour)

	final_url = generate_url(target_time, current_hour)

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
	index = 0
	
	for row in result:
		if target_time in row:
			index = row.index(target_time)

			break 


	api_reading = result[44][index]

	if 	api_reading == "" or \
		api_reading == "n/a":

		print "empty result"
		print "Scrape DONE"
		print "------------------------"
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
			print "------------------------"
			return api_reading

		else:
			print "current API reading: "
			print api_reading
			print "Scrape DONE"
			print "------------------------"
			return api_reading


def previous(time):

	print "Previous function running"


	current_hour = get_current_hour(time)
	target_time = get_target_time(current_hour)

	final_url = generate_url(target_time, current_hour)

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


def get_previous_hour(current_hour):

	if current_hour == 0:
		current_hour = 11
		return current_hour

	else:
		current_hour = current_hour -1
		return current_hour

# previous()
	# Find PJ's index (44)
	# for row in result:
	# 	if 'Nilai' in row:
	# 		print "Nilai"
	# 		print result.index(row) 	
	# 		break 

# target_time = get_target_time()
# current_hour = get_current_hour()
# scrape_website(target_time, current_hour)
