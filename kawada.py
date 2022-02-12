import datetime

time1 = '10:05'

time1 = datetime.datetime.strptime(time1, '%H:%M')
print(time1)

date2 = '20220212'

date2 = datetime.datetime.strptime(date2, '%Y%m%d')
print(date2)

today = datetime.date.today()
print(f"今日{today}")

#
# str = '10/05'
# dte = datetime.datetime.strptime(str, '%H:/%M').time()
# print(type(dte))
# print(dte)
