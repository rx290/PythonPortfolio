"""Write a Python program to print next 5 days starting from today.  """ 

from datetime import date,timedelta

currentDate = date.today()
print("Today's Date: ",currentDate)

for i in range(0,5):
    print("Date on day ",i+1,": ",currentDate+timedelta(days=i))