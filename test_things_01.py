import os
import exrates
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def my_func(aaa, bbb, **time_frame):
    for key, value in time_frame.items():
        if key == 'days':
            time_frame = value
        elif key == 'weeks':
            time_frame = value*7
        else:
            print(f'Method does not accept input param: {time_frame}. Only days or weeks')
            return False

    print(f'{aaa} {bbb}')
    return time_frame


def func_num(aaa, bbb, days=None, weeks=None):
    try:
        if days is not None and weeks is not None:
            print(f'Cannot accept two params at the same time')
        elif days is None and weeks is None:
            print(f'At lease one of the params (days or weeks) need to hold value')
        elif days is not None:
            print(f'days value is: {days}')
        elif weeks is not None:
            print(f'weeks value is: {weeks}')
    except:
        print('Error')


if __name__ == '__main__':
    print('Starting...')
    # time = my_func('hello', 'world', daysr=5)

    # ar = np.array([[1, 3], [2, 5]], dtype=int)
    # print(ar)

    # func_num('Assaf', 'Aloni', dayss=15)

    if os.path.exists(exrates.Exrates.currencies_file_path):
        path = os.path.join(exrates.Exrates.DIR_NAME, 'currencies__.csv')
        my_csv_content = pd.read_csv(path, encoding='UTF-8')
        print(f'The object type is: {type(my_csv_content)}.\n\nThe object  content is:\n{my_csv_content}\n')
        print(f'{my_csv_content.T}\n\n')
        print(f'{my_csv_content.shape}')

