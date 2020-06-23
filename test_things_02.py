import os


date = '2014-06-20'
path = os.path.join('exchange_rates_data', f'ex_rates_{date}.csv')
if os.path.exists(path):
    print('exist')