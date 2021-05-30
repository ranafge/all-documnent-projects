import pprint
data = [{'complete': True, 'volume': 2290, 'time': '2021-01-15',  'mid': {'o': '0.77540', 'h': '0.77584', 'l': '0.77292', 'c': '0.77440'}},  {'complete': True, 'volume': 2312, 'time': '2021-01-15',  'mid': {'o': '0.77436', 'h': '0.77521', 'l': '0.77206', 'c': '0.77206'}}]

pprint.pprint(data)
print(data[0]['mid'])
print(data[1]['mid'])
