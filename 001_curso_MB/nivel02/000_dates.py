# dates (fechas)
from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
# el hora y fecha de este momento mejor utilizado en codigo en timestam
print(now)
year_2023 = datetime(2023,1,1)
print(year_2023)

print('\n**************')
# time
from datetime import time

current_time = time()
print(current_time.hour)
print(current_time.minute)
print(current_time.min)
print(current_time.second)

print('\n**************')
#date
from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 30)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

print('\n**************')
# deltatime
from datetime import timedelta

start_timedelta = timedelta(200,100,100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + end_timedelta)


