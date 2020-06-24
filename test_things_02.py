import exrates
import re


exrt = exrates.Exrates()
user_input = '1998-14-21'
print(exrt.date_validation(user_input))


# text = '2006-11-24'
# if re.search('[1-2][0-9][0-9][0-9][-][0-1][0-9][-][0-3][0-9]', text):
#     print('OK')
# else:
#     print('No match')