""" Write a Python program to add year(s) with a given date and display the new date. 

Sample Data : (addYears is the user defined function name)
print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))

Expected Output :
2014-01-01
2015-01-01
2017-01-01
2001-03-01""" 

from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

def addYears(fullDate,numberOfYear):
    parmDate = datetime.strptime(fullDate,'%Y,%m,%d')
    if (numberOfYear<0):
        return parmDate - relativedelta(years=abs(numberOfYear))
    else:
        return parmDate +relativedelta(years=numberOfYear)

print(addYears('2015,1,1', -1))
print(addYears('2015,1,1',  0))
print(addYears('2015,1,1',  2))
print(addYears('2000,2,29', 1))