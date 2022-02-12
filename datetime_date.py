import calendar
from datetime import date

today = date.today()
print(today)             # 2022-01-21
print(today.year)        # 2022
print(today.month)       # 1
print(today.day)         # 21

date_1 = date(2022, 1, 21)
date_2 = date(2021, 1, 21)
diff = date_1 - date_2
print(diff)             # 365 days, 0:00:00
print(type(date_1))     # <class 'datetime.date'>
print(type(date_2))     # <class 'datetime.date'>
print(type(diff))       # <class 'datetime.timedelta'>


today = date.today()
my_birthday = date(today.year, 3, 5)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
print(my_birthday)                                                  # 2022-03-05
days_until_birthday = my_birthday - today
print('You will celebrate your birthday in', days_until_birthday.days, 'days!')
# You will celebrate your birthday in 43 days!

today = date.today()
week_day = today.weekday()
print(week_day)                                # 4


year = int(input('Please enter a year '))
month = int(input('Please enter a month '))
day = int(input('Please enter a day '))
user_input = date(year, month, day)
print(user_input, 'is a', calendar.day_name[user_input.weekday()])


