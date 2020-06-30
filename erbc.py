import exrates
import datetime
import matplotlib.pyplot as plt


user_input = input("Please type in a date in the format of YYYY-MM-DD: ")
# user_input = '2018-03-12'
currency_code = 'ILS'
exrt = exrates.Exrates()
ils_values = exrt.get_exrate_by_code(currency_code, user_input)
# print(ils_values)

dates_list = list()
currency_rate_list = list()

for key, value in ils_values.items():
    dates_list.append(key)
    currency_rate_list.append(float(value))

new_dates_list = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates_list]
print(new_dates_list)
print(currency_rate_list)

plt.plot(new_dates_list, currency_rate_list)
plt.gcf().autofmt_xdate()
plt.title(f'Exchange rates for {currency_code} from {user_input}')
# plt.xticks(rotation=90)
plt.show()
