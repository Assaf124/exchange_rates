import exrates


exrt = exrates.Exrates()
currencies = exrt.get_currencies()
# print(currencies)
# user_input = input("Please type in a date in the format of YYYY-MM-DD: ")
user_input = '2007-03-12'

exrate_data = exrt.get_exrates(user_input)
print(exrate_data)

# for key, value in exrt.currencies.items():
#     if key in exrt.exchange_rates.keys():
#         print(f'{value} ({key})')
#     else:
#         print(f'({key})')

