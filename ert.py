#   Stands for 'Exchange Rates Table'.  It inputs a date and prints the exchange rates
#   for that date in a tabular form, sorted by the currencies names, with the first column
#   containing the string in the form "Name (code)" and the second one containing the exchange
#   rate relative to the USD, aligned to the right and written to the 5 digits precision.
#
#   The data has to be retrieved using the get_exrates function.

import  exRates
import  sys
import  os
import  logging


#   create logging directory
dir     =   os.getcwd()
logDir  =   os.path.join(dir, 'logging')
if not os.path.exists(logDir):
    os.makedirs(logDir)



logging.basicConfig(    format='%(asctime)s.%(msecs)03d\t\t%(levelname)s:\t%(module)s:\t%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='logging\\program.log',
                        filemode='w',
                        level=logging.DEBUG )

logging.info('\t\t*** program started ***')


try:
    print('****** Exchange Rates Table ******')

    date = input('\nPlease Enter a date value in the format of YYYY-MM-DD: ')

    for i in range(4):
        val = exRates.validateDate(date)

        if val == False:
            if i < 3:
                date = input('\nThere is no such a date. Please try again: ')
                logging.warning('\tuser input data for specific date found to be wrong {}'.format(i))
                continue

            else:
                print('\nThere is no such a date.')
                logging.error('\tuser did not type date correctly. program terminated')
                sys.exit()

        else:
            logging.info('\t\tuser applied a valid date data')
            break

    currencies = exRates._fetch_currencies()
    exRateDict = exRates.get_exrates(date)

    if (currencies == False or exRateDict == False):
        print('Was unable to fetch currencies and/or exchange rates data.')
        logging.warning('\twas unable to fetch currencies and/or exchange rates data')
        sys.exit()


    currenciesAsList = [(v, k) for k, v in currencies.items()]
    currenciesAsList.sort()

    exRateList = exRateDict.items()

    print('\n{:41s} ({}) {}'.format('Currency Name', 'Code', '  Rate'))

    for code2, rate in exRateList:
        flag = 0
        for name, code1 in currenciesAsList:
            if code1 == code2:
                print('{:41s} ({}) {:2s} {}'.format(name, code1, '|', rate))
                flag = 1
                break

        if flag == 0:
            print('{:41s} ({}) {:2s} {}'.format(' ', code2, '|', rate))

    logging.info('\t\tgenerated Exchange Rates Table successfully')

except:
    logging.error('\t\tthe program encountered a problem and has to terminate')
    print('The program encountered a problem and has to terminate')
