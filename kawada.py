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

buy_tickets = [('蒲郡', '7', datetime.time(18, 5), '2連単', 1, 4, 1, 10, datetime.date(2022, 2, 13)),
               ('蒲郡', '7', datetime.time(18, 5), '2連単', 1, 4, 1, 10, datetime.date(2022, 2, 13))]
for i in range(0, len(buy_tickets)):
    place_name = buy_tickets[i][0]
    race_number = buy_tickets[i][1]
    start_time = buy_tickets[i][2]
    ticket_type = buy_tickets[i][3]
    first＿arrival = buy_tickets[i][4]
    second＿arrival = buy_tickets[i][5]
    bet = buy_tickets[i][6]
    deposit = buy_tickets[i][7]
    date = buy_tickets[i][8]
    print(place_name, race_number, start_time, ticket_type, first＿arrival, second＿arrival)
