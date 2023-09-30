"""Write a Python program to get week number. 
Sample Date : 2015, 6, 16
Expected Output : 25 """ 

from datetime import datetime

currentdate = input("Please enter current date: ")
datetimeObj= datetime.strptime(currentdate, '%Y,%m,%d')
print(datetime.strftime(datetimeObj,'%U'))