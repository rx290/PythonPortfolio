""" Write a Python program to convert a string to datetime. 
Sample String : Jan 1 2014 2:43 PM
Expected Output : 2014-01-01 14:43:00 """ 

from datetime import datetime
date_time = input("Please enter your date time string: ")
converted_time = datetime.strptime(date_time, '%b %d %Y %I:%M %p')
print(converted_time.strftime("%Y-%m-%d %H:%M:%S "))