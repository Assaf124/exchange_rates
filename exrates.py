from urllib.request import urlopen
import  json
import  time
import  os
import  ast
import  logging



def _fetch_currencies(*args):

    #   fetches the currencies list from here:
    #   http://openexchangerates.org/api/currencies.json
    #   and returns it as a dictionary

    try:
        response    =   urlopen("http://openexchangerates.org/api/currencies.json")
        currJson    =   response.read()
        dict        =   json.loads(currJson)

        logging.info('fetched currencies successfully from the net')
        return dict

    except  (Exception) as arg:
        print(arg)
        logging.error('was unable to fetch currencies from the net!')
        return False



def _fetch_exrates(date, *args):

    #   fetches the exchange rates of a specific date from the
    #   Open Exchange Rates website (https://openexchangerates.org/)
    #   and returns it as a dictionary

    try:
        if validateDate(date) == False:
            return False

        response    =   urlopen("http://openexchangerates.org/api/historical/" + date + ".json?app_id=b028bbce16ba4164a4e98211dff8d23f")
        ratesJson   =   response.read()
        dict        =   json.loads(ratesJson)
        dict        =   dict["rates"]

        logging.info('fetched exchange rates successfully from the net')
        return dict

    except:
        logging.error('was unable to fetch exchange rates from the net!')
        return False



def _save_currencies(currencies, *args):

    #   Saves the dictionary currencies in the currencies file in a
    #   subdirectory with the name "data" in the current directory.
    #   under the name currencies.csv

    try:
        fname   =   "currencies.csv"
        dir     =   os.getcwd()
        dataDir =   os.path.join(dir , 'data')

        if not os.path.exists(dataDir):
            os.makedirs(dataDir)

        path    =   os.path.join(dataDir,fname)

        currAsCSV   =   createCSVFile(currencies,  'Code' , 'Name')

        file    =   open(path , "w")
        file.write(currAsCSV)
        file.close()

        logging.info('saved currencies successfully')
        logging.debug('')
        return True

    except:
        logging.error('was unable to save currencies!')
        return False



def _save_exrates(date, rates, *args):

    #   Saves the exchange rates data, for a specific date, in the appropriate exchange rates file.
    #   A file with exchange rates for date YYYY-MM-DD should be named rates-YYYY-MM-DD.csv
    #   The file should be saved in subdirectory named 'data'.

    try:
        if validateDate(date) == False:
            return False

        fname   =   'rates-' + date + '.csv'
        dir     =   os.getcwd()
        dataDir =   os.path.join(dir , 'data')

        if not os.path.exists(dataDir):
            os.makedirs(dataDir)

        path = os.path.join(dataDir, fname)

        ratesAsCSV  =   createCSVFile(rates, 'Code', 'Rate')

        file    =   open(path , "w")
        file.write(ratesAsCSV)
        file.close()

        logging.info('saved ex-rates successfully')
        return True

    except:
        logging.error('was unable to save ex-rates!')
        return False



def _load_currencies():

    #   returns the currencies loaded from the currencies file.

    try:
        fname   =   "currencies.csv"
        dir     =   os.getcwd()
        dataDir =   os.path.join(dir, 'data')

        if not os.path.exists(dataDir):
            return False

        path    =   os.path.join(dataDir, fname)

        aFile       =   open(path, 'r')
        currencies  =   aFile.read()
        aFile.close()

        logging.info('loaded currencies successfully')
        return currencies

    except:
        logging.error('was unable to load currencies!')
        return False



def _load_exrates(date):

    #   returns the exchange rates data for specific date
    #   from appropriate exchange rates file

    try:
        fname   =   'rates-' + date + '.csv'
        dir     =   os.getcwd()
        dataDir =   os.path.join(dir, 'data')
        path    =   os.path.join(dataDir, fname)

        if os.path.exists(path):
            aFile   =   open(path, 'r')
            rates   =   aFile.read()
            aFile.close()

            logging.info('loaded ex-rates successfully')
            return rates

        else:
            logging.warning('Rates.csv file was not found.')
            return 'Rates.csv file was not found.'

    except:
        logging.error('was unable to load ex-rates!')
        return False



def get_currencies():

    #   Returns the currencies loaded from the currencies file, as a dictionary.
    #   If the currencies file doesn't exists, the function fetches the data from
    #   the internet, saves it to the currencies file and then returns it.

    try:
        fname   =   "currencies.csv"
        dir     =   os.getcwd()
        dataDir =   os.path.join(dir, 'data')
        path    =   os.path.join(dataDir, fname)

        #   If currencies.csv file does not exist making one try to create it

        if not os.path.exists(path):
            currReply   =   _fetch_currencies()
            if currReply == False:
                logging.error('was unable to fetch currencies from the net!')
                return False

            saveCuReply = _save_currencies(currReply)
            if saveCuReply == False:
                logging.error('was unable to save currencies fetched from the net!')
                return False


        if not os.path.exists(path):
            return False

        aFile       =   open(path, 'r')
        currStr     =   aFile.read()
        aFile.close()

        currStr     =   currStr.replace('\n' , ',')
        currLst     =   currStr.split(',')

        currDict    =   dict(zip(currLst[0::2], currLst[1::2]))
        del currDict['Code']

        logging.info('got currencies from local .csv file successfully')
        return currDict


    except:
        logging.error('was unable to get currencies from local .csv file!')
        return False



def get_exrates(date):

    #   Returns the exchange rates data for the date 'date' loaded from the appropriate
    #   exchange rates file. If that file doesn't exists, the function fetches the
    #   data from the internet, saves it to the file, and then returns it.

    try:
        fname   =   'rates-' + date + '.csv'
        dir     =   os.getcwd()
        dataDir =   os.path.join(dir, 'data')
        path    =   os.path.join(dataDir, fname)

        #   If rates.csv file does not exist for that date then making one try to create it

        if not os.path.exists(path):
            ratesReply  =   _fetch_exrates(date)
            if ratesReply == False:
                return False

            saveRaReply =   _save_exrates(date, ratesReply)
            if saveRaReply == False:
                return False


        if not os.path.exists(path):
            return False

        aFile       =   open(path, 'r')
        rateStr     =   aFile.read()
        aFile.close()

        rateStr     =   rateStr.replace('\n' , ',')
        rateLst     =   rateStr.split(',')

        rateDict    =   dict(zip(rateLst[0::2], rateLst[1::2]))
        del rateDict['Code']

        logging.info('got ex-rates from local .csv file successfully')
        return rateDict


    except:
        logging.error('was unable to get ex-rates from local .csv file!')
        return False



def validateDate(date, *args):

    #   This function validates that 'date' value is in the format of YYYY-MM-DD

    try:
        time.strptime(date, '%Y-%m-%d')

        today = time.strftime("%Y-%m-%d", time.gmtime())

        if date > today:
            return False

        else:
            return True


    except ValueError:
        return False



def createCSVFile(inFile, header1, header2, *args):

    #   This function converts a dictionary to a string in a csv format.

    str1    =   ast.literal_eval(json.dumps(inFile))
    str1    =   str(str1)
    str1    =   str1.replace(', ' , '\n')
    str1    =   str1.replace(': ' , ',')
    str1    =   str1.replace("'" , "")
    str1    =   str1.replace('{' , '')
    str1    =   str1.replace('}' , '')
    str1    =   str1.strip()
    str1    =   '{},{}\n{}'.format(header1, header2,str1)

    logging.info('created .csv file successfully')
    return str1
