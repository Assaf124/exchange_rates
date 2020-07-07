
def my_func(aaa, bbb, **time_frame):
    # time_frame = None
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


if __name__ == '__main__':
    print('Starting...')
    time = my_func('hello', 'world', days=5)
    print(time)

