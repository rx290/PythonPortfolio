""" Write a Python program to print yesterday, today, tomorrow.  """ 
from datetime import date, datetime, timedelta

print("Yesterday: ",date.today()+ timedelta(days=-1)," Today: ",date.today()," Tomorrow: ",date.today()+ timedelta(days=1))
