The aim of the exercise is to design and develop a system for efficient management of the historic currency exchange rates.


Write a module exrates that implements fetching, saving, and analysis of the historical exchange rates. The module has to provide the following functions:

•	_fetch_currencies() that fetches the currencies list from here (http://openexchangerates.org/api/currencies.json) and returns it as a dictionary (see the description of the format below).
•	_fetch_exrates(date) that fetches the exchange rates for the date date from the Open Exchange Rates (https://openexchangerates.org/) website and returns it as a dictionary (see the description of the format below).
•	_save_currencies(currencies) that saves the dictionary currencies in the currencies file, as described below.
•	_save_exrates(date, rates) that saves the exchange rates data for date date in the appropriate exchange rates file, as described below.
•	_load_currencies() that returns the currencies loaded from the currencies file. 
•	_load_exrates(date) that returns the exchange rates data for date date loaded from the appropriate exchange rates file.
•	get_currencies() that returns the currencies loaded from the currencies file, as a dictionary. If the currencies file doesn't exists, the function fetches the data from the internet, saves it to the currencies file and then returns it.
•	get_exrates(date) that returns the exchange rates data for date date loaded from the appropriate exchange rates file. If that file doesn't exists, the function fetches the data from the internet, saves it to the file, and then returns it.

The functions have to raise proper exceptions on invalid input or if they cannot perform their tasks for some other reason (for example, a failed network connection or badly formated data).

The module must also create the data directory if it doesn't already exist. For this purpose, consider using the os.makedirs (https://docs.python.org/3/library/os.html#os.makedirs) and os.path.exists (https://docs.python.org/3/library/os.path.html#os.path.exists) functions.



Using the module exrates, write the following programs: 
1.	cod (which stands for Currencies On a Date), that inputs a date and prints the list of currencies for which there is a data on that date (i.e., the keys for the exchange rates dictionary on that date). The currencies should be printed in the format "Name (code)", one per line, sorted by their code. Of course, the names are obtained from the currencies list. However, some may be missing there (for the currencies that don't exist anymore, like SIT that existed in the database between 2003-06- 02 and 2006-12-22). Those should be printed as " (code)". 

2.	ert (which stands for Exchange Rates Table), that inputs a date and prints the exchange rates for that date in a tabular form, sorted by the currencies names, with the first column containing the string in the form "Name (code)" and the second one containing the exchange rate relative to the USD, aligned to the right and written to the 5 digits precision. The data has to be retrieved using the get_exrates function.

3.	erbc (which stand for Exchange Rates by Currency) that inputs currency code and date and prints a graph with currency rates for the past 52 weeks 

