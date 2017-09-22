# Scraping-find-max
Scrape data from the website OKCoin and find the transactions with maximum priced or minimun priced.

### Version
1.0.0

### Installation
For json_find_max.py, please interpret it with Python 2.7
For find_max.py, please interpret it with Python 3.6
Or, you can simply edit the print function.

### json_find_max.py
This program reads the 'foo.txt'(the target file can be named after what you like).
Since the content of 'foo.txt' is in the format of JSON, I use the 'json.load()' method to read the data.
I use the max function with simple technique, lambda function, to find the item with maximum priced.
Finally, show the maximum priced and minimun priced transactions' ID and price respectively.

### find_max.py
The simplified version of above program, json_find_max.py.
