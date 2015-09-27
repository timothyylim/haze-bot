

import requests
from datetime import datetime
from bs4 import BeautifulSoup

def test_function():
	# Check the we are on the right page for the hour 
	right_page = False 

	current_hour = str(datetime.now().hour)
	d = datetime.strptime(current_hour, "%H")
	d = d.strftime("%I:%M%p")
	target_time = str(d)


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
	import time
	date_url = str((time.strftime("%Y-%m-%d")))+".html"


	###############
	# put it all together 
	###############

	final_url = starting_url+hour_url+date_url




	r = requests.get("http://apims.doe.gov.my/v2/hour3_2015-09-27.html")
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
				redone_output = output[17:24]
				result[-1].append(redone_output)

			else:

				value = cell.string
				value = value.encode('ascii', 'ignore').decode('ascii')
				string_value = str(value)
				result[-1].append(string_value)

	index = 0

	for row in result:
		if target_time in row:
			index = row.index(target_time)

			right_page = True 
			break 


	# Find PJ's index (44)
	# for row in result:
	# 	if 'Nilai' in row:
	# 		print "Nilai"
	# 		print result.index(row) 	
	# 		break 


	# print result[12]
	api_reading = result[12][4]


	if 	api_reading == "" or \
		api_reading == "n/a":

		print "empty"

	else:
		if 	api_reading.endswith('*') or \
			api_reading.endswith('a') or \
			api_reading.endswith('b') or \
			api_reading.endswith('c') or \
			api_reading.endswith('&'):
			reading_length = len(api_reading)
			
			api_reading = api_reading[:reading_length-1]
			print api_reading
			

test_function()
