code = 'AMD'
my_dict = {'AED': '3.67303', 'AFN': '56.870351', 'ALL': '101.816499', 'AMD': '416.132998', 'ANG': '1.78702'}

for key, value in my_dict.items():
    if key == code:
        print(f'{key} | {value}')




