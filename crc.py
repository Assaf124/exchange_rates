# crc stand for currencies comparison
import exrates
import datetime
import matplotlib.pyplot as plt


# date_input = input("Please type in a date in the format of YYYY-MM-DD: ")
date_input = '2016-03-12'
# first_currency_input = input("Please type in a valid currency code: ")
first_currency_input = 'EUR'
# second_currency_input = input("Please type in a valid currency code: ")
second_currency_input = 'ILS'
# time_frame_type = input("Please select time frame (days|weeks): ")

# time_frame_period = input("Please select time frame period: ")


exrt = exrates.Exrates()
currency_tuple = exrt.compare_exrates(first_currency_input, second_currency_input, date_input, weeks=6)
# print(currency_tuple)


dates_list_1 = list()
dates_list_2 = list()
currency_rate_list_1 = list()
currency_rate_list_2 = list()

for key, value in currency_tuple[0].items():
    dates_list_1.append(key)
    currency_rate_list_1.append(float(value))

for key, value in currency_tuple[1].items():
    dates_list_2.append(key)
    currency_rate_list_2.append(float(value))

# Generating the graph

fig = plt.figure()
ax = fig.gca()
ax.set_title(f'{first_currency_input} Vs {second_currency_input} compared to USD')
ax.set_ylabel(f'{first_currency_input}')
ax.yaxis.label.set_color('b')
ax.tick_params(axis='y', colors='blue')
ax.set_xlabel(f'Dates')

ax2 = ax.twinx()
ax2.set_ylabel(f'{second_currency_input}')
ax2.yaxis.label.set_color('r')
ax2.spines['right'].set_color('red')
ax2.tick_params(axis='y', colors='red')

line1, = ax.plot(dates_list_1, currency_rate_list_1, '-', color='#1E90FF')
line2, = ax2.plot(dates_list_2, currency_rate_list_2, '--', color='#DC143C')

ax.legend([line1, line2], [f'{first_currency_input}', f'{second_currency_input}'])
plt.xticks(rotation=45)
plt.show()
