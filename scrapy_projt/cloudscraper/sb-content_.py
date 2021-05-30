rstocks = ['5.57%', '3.95%', '5.26%', '5.49%', '-1.80%']

stocks = []
for x in rstocks:
    stocks.append(float(x.strip('%'))*100)
print(stocks)

print(stocks)
[557.0, 395.0, 526.0, 549.0, -180.0]
