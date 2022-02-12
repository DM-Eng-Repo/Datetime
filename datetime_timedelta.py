from datetime import timedelta, datetime

print(timedelta())   # 0:00:00
year = timedelta(days=365)
print(year)           # 365 days, 0:00:00

today = datetime.now()
print('Today is', today)     # Today is 2022-01-28 16:16:41.684476

print('23 days from today will be', (today + timedelta(days=23)))
# 23 days from today will be 2022-02-20 16:18:56.470838
print('93 days from today will be', (today + timedelta(days=93)))
# 93 days from today will be 2022-05-01 16:21:51.141189
print('45 days from today will be', (today + timedelta(days=45)))
# 45 days from today will be 2022-03-14 16:21:51.141189

print('230000 seconds from today will be', (today + timedelta(seconds=230000)))
# 230000 seconds from today will be 2022-01-31 08:17:48.781658

today = datetime.now()
last_birthday = datetime(2021, 3, 5)
print(f'My last birthday was {(today - last_birthday).days} days ago.')
# My last birthday was 329 days days ago.

year = timedelta(days=365)
print(f'There are {year.total_seconds()} seconds in a year.')
# There are 31536000.0 seconds in a year.

print(f'There are {(year * 7).days} days in 7 years.')
# There are 2555 days in 7 years.
