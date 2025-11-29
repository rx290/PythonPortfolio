""" Write a Python program to subtract five days from current date. 
Sample Date :
Current Date : 2015-06-22
5 days before Current Date : 2015-06-17 """ 

from datetime import timedelta, date

current_date = date.today()
date_after_5_days = current_date + timedelta(days=-5)

print("Current Date:",current_date,"\n5 days before Current Date: ",date_after_5_days)