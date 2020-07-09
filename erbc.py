# erbc stand for exchange rate by currency
import exrates
import datetime
import matplotlib.pyplot as plt


date_input = input("Please type in a date in the format of YYYY-MM-DD: ")
# user_input = '2017-03-12'
currecny_input = input("Please type in a valid currency code: ")
# currecny_input = 'EUR'
exrt = exrates.Exrates()
ils_values = exrt.get_exrate_by_code(currecny_input, date_input, weeks=8)

dates_list = list()
currency_rate_list = list()

for key, value in ils_values.items():
    dates_list.append(key)
    currency_rate_list.append(float(value))

new_dates_list = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates_list]

plt.plot(new_dates_list, currency_rate_list)

plt.gcf().autofmt_xdate()
plt.title(f'Exchange rates for {currecny_input} up to {date_input}')
# plt.xticks(rotation=90)
plt.show()
