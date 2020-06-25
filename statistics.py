import exrates
import datetime
import matplotlib.pyplot as plt


# user_input = input("Please type in a date in the format of YYYY-MM-DD: ")
exrt = exrates.Exrates()
# exrt.get_exrates(user_input)

# current_date = datetime.datetime.now()
# date = str(current_date)
# date_list = date.split(' ')
# today = date_list[0]
# # print(today)
# exrt.get_exrate_by_code(today, 'ILS')
# print(exrt.get_exrate_by_code(today, 'ILS'))

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
