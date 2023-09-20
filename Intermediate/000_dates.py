### Dates ###

from datetime import datetime

now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()

print (timestamp)



def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
print_date(now)

year_2023 = datetime(2023,1,1)

print_date(year_2023)

from datetime import time

current_time = time()

print(current_time.hour)
print(current_time.minute)
print(current_time.second)
    

from datetime import date

current_date = date(1993,1,8)
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)

from datetime import timedelta

time_delta = timedelta()




