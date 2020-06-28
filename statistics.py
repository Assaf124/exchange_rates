import exrates
import datetime
import matplotlib.pyplot as plt


# user_input = input("Please type in a date in the format of YYYY-MM-DD: ")
date = '2018-03-12'
exrt = exrates.Exrates()
ils_values = exrt.get_exrate_by_code('ILS', date)
# print(ils_values)

dates_list = list()
currency_rate_list = list()

for key, value in ils_values.items():
    dates_list.append(key)
    currency_rate_list.append(value)

plt.plot(dates_list, currency_rate_list)
plt.xticks(rotation=90)
# plt.axis()
plt.show()
