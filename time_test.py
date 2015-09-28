from datetime import datetime
from pytz import timezone    

malaysia_time = timezone('Asia/Kuala_Lumpur')
# malaysia_time = datetime.now(malaysia_time)
# malaysia_date_url = str(malaysia_time.strftime('%Y-%m-%d')) + ".html"
# print malaysia_time.strftime('%Y-%m-%d')
# print str(malaysia_time.strftime('%Y-%m-%d')) + ".html"

# malaysia_date_url = str(malaysia_time.strftime('%Y-%m-%d')) + ".html"

# import time
# date_url = str((time.strftime("%Y-%m-%d")))+".html"
# print date_url

# if date_url == test_date:
# 	print "yest"
current_hour = str(datetime.now().hour)
d = datetime.strptime(current_hour, "%H")
d = d.strftime("%I:%M%p")
target_time = str(d)
print "first"
print target_time



current_hour1 = str(datetime.now().hour)
d1 = datetime.strptime(current_hour1, "%H")
d1 = d1.strftime("%I:%M%p")
target_time1 = str(d1)
print "second"
print target_time1
