import datetime

mytime = datetime.time(2,20) # 24 hour type
print("minute ",mytime.minute)
print("mytime ",mytime)

today = datetime.date
print("today ",today.today())
print("year ",today.today().year)

from datetime import datetime

mydatetime = datetime(2024,2,10,22,17)
print("mydatetime ",mydatetime)
print("replace ",mydatetime.replace(minute=18))

from datetime import date

date1 = date(2024,12,4)
date2 = date(2023,12,4)

print("differnce ",(date1 - date2))