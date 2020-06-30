import requests
import os
import re
import datetime
import time


class Exrates:
    APP_ID = 'b028bbce16ba4164a4e98211dff8d23f'
    DIR_NAME = 'exchange_rates_data'
    CURRENCIES_FILE_NAME = 'currencies.csv'
    currencies_file_path = os.path.join(DIR_NAME, CURRENCIES_FILE_NAME)

    def __init__(self):
        self.currencies = dict()
        self.exchange_rates = dict()
        self.exchange_rates_by_code = dict()
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

    def date_validation(self, date: str):
        """
        Validates the date input is in the format of YYYY-MM-DD
        :param date:    string. date info in the format YYYY-MM-DD
        :returns:       True
                        False
        """
        if re.search('[1,2][0,9][0-9][0-9][-][0,1][0-9][-][0-3][0-9]', date):
            return True
        else:
            return False

    def _fetch_exrates(self, date: str, *args):
        """
        Fetches the exchange rates for the date date from the Open Exchange Rates
        website (https://openexchangerates.org/) and returns it as a dictionary.
        :param date:    string. date info in the format YYYY-MM-DD
        :return:        dictionary
                        None
        """
        try:
            url = f'http://openexchangerates.org/api/historical/{date}.json?app_id={Exrates.APP_ID}'
            response = requests.get(url, verify=False)
            self.exchange_rates = response.json()
            self.exchange_rates = self.exchange_rates['rates']
            return self.exchange_rates

        except Exception as error:
            print(f'was  unable to fetch exchange rates. got: {error}')
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

    def _save_currencies(self, currencies: dict):
        """
        Saves the dictionary currencies as a csv file.
        :param currencies:  dictionary
        :return:            True
                            False
        """
        self.create_dir()
        currencies_as_csv = self._convert_currencies_to_csv(currencies)
        try:
            path = Exrates.currencies_file_path
            with open(path, 'w') as file:
                file.write(str(currencies_as_csv))
                file.close()
            return True

        except Exception as error:
            print(f'{error}')
            return False

    def _save_exrates(self, date: str, rates_info: dict):
        """
        Saves the exchange rates data for date date in the appropriate exchange rates file.
        :param date:        string. date info in the format YYYY-MM-DD
        :param rates_info:  dictionary. exchange rates information
        :return:            True
                            False
        """
        self.create_dir()
        rates_as_csv = self._convert_exrates_to_csv(rates_info)
        try:
            path = os.path.join(Exrates.DIR_NAME, f'ex_rates_{date}.csv')
            with open(path, 'w') as file:
                file.write(str(rates_as_csv))
                file.close()
            return True

        except Exception as error:
            print(f'{error}')
            return False

    def _load_currencies(self):
        """
        Loads currencies info from drive, convert it from string/csv format
        to python dictionary and returns it
        :return:    dictionary
                    None
        """
        try:
            file_obj = open(Exrates.currencies_file_path, 'r')
            file_content = file_obj.read()
            file_as_list = re.split('[\n,]', file_content)

            for index, item in enumerate(file_as_list[:-1]):
                if index % 2 != 0:
                    continue
                self.currencies[item] = file_as_list[index + 1]
            return self.currencies

        except Exrates as error:
            print(f'{error}')
            return None

    def _load_exrates(self, date: str):
        """
        Loads exchange rates info from drive, convert it from string/csv format
        to python dictionary and returns it
        :param date:    string. date info in the format YYYY-MM-DD
        :returns:       dictionary
                        None
        """
        try:
            path = os.path.join(Exrates.DIR_NAME, f'ex_rates_{date}.csv')
            file_obj = open(path, 'r')
            file_content = file_obj.read()
            file_as_list = re.split('[\n,]', file_content)

            for index, item in enumerate(file_as_list[:-1]):
                if index % 2 != 0:
                    continue
                self.exchange_rates[item] = file_as_list[index + 1]
            return self.exchange_rates

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
            if os.path.exists(Exrates.currencies_file_path):
                return self._load_currencies()
            else:
                currencies = self._fetch_currencies()
                self._save_currencies(currencies)
                return currencies

        except Exception as error:
            print(f'{error}')
            return None

    def get_exrates(self, date: str):
        """
        Returns the exchange rates data for date date loaded from the appropriate exchange rates file.
        If that file doesn't exists, the function fetches the data from the internet, saves it to the
        file, and then returns it.
        :param date:    string. date info in the format YYYY-MM-DD
        :return:        dictionary
                        None
        """
        path = os.path.join(Exrates.DIR_NAME, f'ex_rates_{date}.csv')
        try:
            if os.path.exists(path):
                return self._load_exrates(date)
            else:
                rates = self._fetch_exrates(date)
                self._save_exrates(date, rates)
                return rates

        except Exception as error:
            print(f'{error}')
            return None

    def get_exrate_by_code(self, code: str, date: str):
        """
        Returns specific rate value based on currency code for specific date
        :param code:    string. 3 chars currency code (like USD, ILS etc...)
        :param date:    string. date info in the format YYYY-MM-DD
        :returns:       dictionary. in the format of {'date1': exchange_rate1, 'date2': exchange_rate2...}
                        None
        """
        try:
            fetch_date = self._generate_new_date(date, -365)
            for x in range(13):
                path = os.path.join(Exrates.DIR_NAME, f'ex_rates_{fetch_date}.csv')
                if not os.path.exists(path):
                    self._fetch_exrates(fetch_date)
                    self._save_exrates(fetch_date, self.exchange_rates)
                else:
                    self._load_exrates(fetch_date)

                for key, value in self.exchange_rates.items():
                    if key == code:
                        self.exchange_rates_by_code[fetch_date] = value
                        # print(f'{self.exchange_rates_by_code}')
                        print(f'added key: {fetch_date} and value: {value}')
                time.sleep(5)
                # advancing the date one week
                fetch_date = self._generate_new_date(fetch_date, 7)
            return self.exchange_rates_by_code

        except Exception as error:
            print(f'{error}')
            return None

    def _generate_new_date(self, date: str, delta: int):
        """
        Generates new date based on given date and delta
        :param date:    string. date info in the format YYYY-MM-DD for example 2017-03-12
        :param delta:   integer. the delta in days from the given date in the input to the required date in the 'output'
        :returns:       string in the format of YYYY-MM-DD, for example 2017-03-12
                        None
        """
        try:
            datetime_format = datetime.datetime.strptime(date, '%Y-%m-%d')
            new_date = datetime_format + datetime.timedelta(days=delta)
            date_string = str(new_date)
            date_as_list = date_string.split(' ')
            return str(date_as_list[0])

        except Exception as error:
            print(f'{error}')
            return None

    def _convert_currencies_to_csv(self, currencies_file: dict):
        """
        Converts the currencies file fetched by _fetch_currencies to csv file format
        :param currencies_file: dictionary. in the format of {'name': 'code'...}
        :return:                string. csv file format
        """
        currencies = ''
        for key, value in currencies_file.items():
            currencies += value
            currencies += ','
            currencies += key
            currencies += '\n'
        return currencies

    def _convert_exrates_to_csv(self, exrates_file: dict):
        """
        Converts the ex-rates file fetched by _fetch_exrates to csv file format
        :param exrates_file:    dictionary. in the format of {'code': 'ex_rate'...}
        :return:                csv file format
        """
        exrates = ''
        for key, value in exrates_file.items():
            exrates += key
            exrates += ','
            exrates += str(value)
            exrates += '\n'
        return exrates


if __name__ == '__main__':
    date = '2014-11-14'
    aaa = Exrates()
    print(aaa._generate_new_date(date, -7))
    # print(aaa.date_validation(date))
    # currencies = aaa.get_currencies()
    # print(currencies)
    # rates = aaa.get_exrates(date)
    # print(rates)
    ils_values = aaa.get_exrate_by_code('ILS', date)
    print(ils_values)
