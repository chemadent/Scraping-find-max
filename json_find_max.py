#!/usr/bin/env python
# coding: utf-8

# Read a txt file whose content is actually in JSON format
# and print out the maximum and the minimum of price and
# their tids respectively.

import sys
import json

file_name = 'foo.txt'
try:
	with open(file_name) as json_file:
		json_str  = json_file.read()
		json_data = json.loads(json_str)
except:
    print sys.exc_info()[0]
    raise

max_priced_item = max(json_data, key=lambda x:x['price'])
min_priced_item = min(json_data, key=lambda x:x['price'])
print "max priced item's price:", max_priced_item['price'],", "\
"tid:", max_priced_item['tid']
print "min priced item's price:", min_priced_item['price'],", "\
"tid:", min_priced_item['tid']