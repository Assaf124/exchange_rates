import numpy as np


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
    time = my_func('hello', 'world', daysr=5)
    print(time)

    # ar = np.array([[1, 3], [2, 5]], dtype=int)
    # print(ar)

    # func_num('Assaf', 'Aloni', dayss=15)

