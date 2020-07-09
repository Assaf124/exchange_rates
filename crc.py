# crc stand for currencies comparison
import exrates
import datetime
import matplotlib.pyplot as plt


# date_input = input("Please type in a date in the format of YYYY-MM-DD: ")
date_input = '2017-03-12'
# first_currency_input = input("Please type in a valid currency code: ")
first_currency_input = 'EUR'
# second_currency_input = input("Please type in a valid currency code: ")
second_currency_input = 'USD'


exrt = exrates.Exrates()

