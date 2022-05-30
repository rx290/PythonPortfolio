"""Write a Python script to display the various Date Time formats - 
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week """ 
from datetime import datetime

print(datetime.utcnow())

print(datetime.today().year)

print(datetime.today().month)

print(datetime.today().isocalendar()[1])

print(datetime.today().weekday())

print(datetime.today().timetuple().tm_yday)

print(datetime.today().day)
