import os
import re

path = os.path.join('exchange_rates_data', 'currencies.csv')
file_obj = open(path, 'r')
file_content = file_obj.read()
print(file_content)

file_as_list = re.split('[\n,]', file_content)
print(file_as_list)

my_dict = dict()
for index, item in enumerate(file_as_list[:-1]):
    if index % 2 != 0:
        continue
    my_dict[item] = file_as_list[index+1]


print(my_dict)



