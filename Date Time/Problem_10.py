"""Write a Python program to add 5 seconds with the current time. 
Sample Data :
13:28:32.953088
13:28:37.953088 """ 

from datetime import datetime,timedelta
currentTime = datetime.now()
print("Current Time: ", currentTime.time())
currentTime5SecondsAhed = currentTime + timedelta(seconds=5)
print("New time with 5 seconds added: ",currentTime5SecondsAhed.time())