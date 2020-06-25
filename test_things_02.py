import exrates
import datetime
import re


exrt = exrates.Exrates()
user_input_date = '2013-09-21'
# print(exrt.date_validation(user_input_date))


end_date = datetime.datetime.strptime(user_input_date, '%Y-%m-%d')
start_date = end_date + datetime.timedelta(days=-365)

start_date_string = str(start_date)
start_date_time = start_date_string.split(' ')
fetch_date = str(start_date_time[0])
print(f'First fetch date: {fetch_date}')

for x in range(5):
    fetch_date = datetime.datetime.strptime(fetch_date, '%Y-%m-%d')
    fetch_date = fetch_date + datetime.timedelta(days=7)
    fetch_date_list = (str(fetch_date)).split(' ')
    # fetch_date_list = fetch_date.split(' ')
    fetch_date = str(fetch_date_list[0])

    print(f'Next date: {fetch_date}')

