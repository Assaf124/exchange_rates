import requests
import os


class Exrates:
    APP_ID = 'b028bbce16ba4164a4e98211dff8d23f'
    DIR_NAME = 'exchange_rates_data'
    CURRENCIES_FILE_NAME = 'currencies.csv'
    currencies_file_path = os.path.join(DIR_NAME, CURRENCIES_FILE_NAME)

    def __init__(self):
        self.currencies = dict()
        self.exchange_rates = dict()
        self.dir_path = ''

    def _fetch_currencies(self):
        """
        Fetches the currencies list from:
        http://openexchangerates.org/api/currencies.json
        and returns it as a dictionary.
        :return:    dictionary
                    None
        """
        try:
            url = f'http://openexchangerates.org/api/currencies.json'
            response = requests.get(url, verify=False)
            self.currencies = response.json()
            return self.currencies

        except Exception as error:
            print(f'was not able to fetch currencies file. got {error}')
            return None

    def date_validation(self, date):
        """
        Validates the date input format + input date is < than today's date.
        """

    def _fetch_exrates(self, date, *args):
        """
        Fetches the exchange rates for the date date from the Open Exchange Rates
        website (https://openexchangerates.org/) and returns it as a dictionary.
        :param:     date
        :return:    dictionary
                    None
        """
        try:
            url = f'http://openexchangerates.org/api/historical/{date}.json?app_id={Exrates.APP_ID}'
            response = requests.get(url, verify=False)
            self.exchange_rates = response.json()
            return self.exchange_rates

        except Exception as error:
            print(f'was not able to fetch exchange rates. got: {error}')
            return None

    def create_dir(self):
        """
        Creates 'Exrate Data Dir'
        :return:    True
                    False
        """
        try:
            os.makedirs(Exrates.DIR_NAME, mode=0o777 ,exist_ok=True)
            return True

        except Exception as error:
            print(f'{error}')
            return False

    def _save_currencies(self, currencies):
        """
        Saves the dictionary currencies as a csv file.
        :param:     currencies
        :return:    True
                    False
        """
        self.create_dir()
        try:
            path = Exrates.currencies_file_path
            # path = os.path.join('exchange_rates_data', 'currencies.csv')
            with open(path, 'w') as file:
                file.write(str(currencies))
                file.close()
            return True

        except Exception as error:
            print(f'{error}')
            return False

    def _save_exrates(self, date, rates_info):
        """
        Saves the exchange rates data for date date in the appropriate exchange rates file.
        :param:     date
        :return:    True
                    False
        """
        self.create_dir()
        try:
            path = os.path.join('exchange_rates_data', f'ex_rates_{date}.csv')
            with open(path, 'w') as file:
                file.write(str(rates_info))
                file.close()
            return True

        except Exception as error:
            print(f'{error}')
            return False

    def _load_currencies(self):
        """
        Returns the currencies loaded from the currencies file.
        :return:    dictionary
                    currencies.csv
        """
        try:
            path = os.path.join('exchange_rates_data', 'currencies.csv')
            file_obj = open(path, 'r')
            file_content = file_obj.read()
            return file_content

        except Exception as error:
            print(f'{error}')
            return None

    def _load_exrates(self, date):
        """
        Returns the exchange rates data for date date loaded from the appropriate exchange rates file.
        :return:    ?
                    None
        """
        try:
            path = os.path.join('exchange_rates_data', f'ex_rates_{date}.csv')
            file_obj = open(path, 'r')
            file_content = file_obj.read()
            return file_content

        except Exception as error:
            print(f'{error}')
            return None

    def get_currencies(self):
        """
        Returns the currencies loaded from the currencies file, as a dictionary.
        If the currencies file doesn't exists, the function fetches the data from the internet, saves it to
        the currencies file and then returns it.
        :return:    dictionary
                    None
        """
        try:
            if self._load_currencies() is not None:
                return self._load_currencies()
            else:
                currencies = self._fetch_currencies()
                self._save_currencies(currencies)
                return currencies

        except Exception as error:
            print(f'{error}')
            return None

    def get_exrates(self, date):
        """
        Returns the exchange rates data for date date loaded from the appropriate exchange rates file.
        If that file doesn't exists, the function fetches the data from the internet, saves it to the
        file, and then returns it.
        :return:    dictionary
                    None
        """
        try:
            ex_rates = self._load_exrates(date)
            if ex_rates is not None:
                return ex_rates
            else:
                ex_rate = self._fetch_exrates(date)
                self._save_exrates(date, ex_rate)
                return ex_rate

        except Exception as error:
            print(f'{error}')
            return None


if __name__ == '__main__':
    date = '2018-08-20'
    aaa = Exrates()
    bbb = aaa.get_exrates(date)
    print(bbb)
    ccc = aaa.get_currencies()
    print(ccc)