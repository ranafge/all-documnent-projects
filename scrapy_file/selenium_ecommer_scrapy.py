import requests
import json
from datetime import datetime
import collections

result = requests.get("https://api.exchangeratesapi.io/history?start_at=2020-12-1&end_at=2020-12-13&symbols=USD,TRY&base=USD")
result = json.loads(result.text)
print(result)
print()
print(result["rates"])
d = result['rates']
order = collections.OrderedDict(sorted(d.items()))
print('order')
print(order)
print()
print(*order.items())
# print(sorted(i, key=lambda date: datetime.strptime(date, "%Y-%m-%d")))
sorted_rates = dict(sorted(
  result["rates"].items(),
  key=lambda item: datetime.strptime(item[0], "%Y-%m-%d")))

print(sorted_rates)
