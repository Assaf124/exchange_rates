import exrates


exrt = exrates.Exrates()
exrt.get_currencies()
# user_input = input("Please type in a date in the format of YYYY-MM-DD: ")
user_input = '2019-05-18'

exrt.get_exrates(user_input)
# print(exrt.exchange_rates)

print(f'Currencies exchange rates info for the date {user_input}:', end='\n\n')

for key, value in exrt.currencies.items():
    if value in exrt.exchange_rates.keys():
        print(f'{key:41s}  {value:2s}  |  {exrt.exchange_rates[value]}')
        # print('{:41s} ({}) {:2s} {}'.format(key, value, '|', exrt.exchange_rates[value]))
