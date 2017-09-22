import json

def price_func(x):
	return x['price']

f = open('foo.txt')
string = f.read()
json_data = json.loads(string)
f.close()

max_priced_item = max(json_data, key=price_func)
min_priced_item = min(json_data, key=price_func)
print("max priced item's price:", max_priced_item['price'], ", tid:", max_priced_item['tid'])
print("min priced item's price:", min_priced_item['price'], ", tid:", min_priced_item['tid'])