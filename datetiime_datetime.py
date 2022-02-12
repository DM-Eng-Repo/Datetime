from datetime import datetime

today = datetime(2022, 1, 28)
print(today)                        # 2022-01-28 00:00:00

today_now = datetime.now()
print(today_now)                    # 2022-01-28 15:11:59.187689

timestamp = datetime.timestamp(today)  # показуэ час выд початку епохи до дати введеної в аргумент
print(timestamp)                    # 1643324400.0

today_from_timestamp = datetime.fromtimestamp(timestamp)
print(today_from_timestamp)                  # 2022-01-28 00:00:00


today_format = today.strftime('%d %B %Y')
print('Today is', today_format)              # Today is 28 January 2022
print('Today is', today.strftime('%A'))      # Today is Friday


today = datetime.today()
print(today)               # 2022-01-28 15:31:53.526516

utc_today = today.utcnow()
print(utc_today)           # 2022-01-28 14:31:53.526516

print(today.date())              # 2022-01-28
print(today.time())              # 15:33:29.239508
print(today.isocalendar())       # datetime.IsoCalendarDate(year=2022, week=4, weekday=5)
print(today.isoformat())         # 2022-01-28T16:09:57.107272
