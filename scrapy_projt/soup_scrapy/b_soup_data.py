
import requests
from lxml import html
import w3lib.html

url = 'https://www.hybrid-analysis.com/sample/a1b38a18decb253708e0198bfaaed97ef1c16fc061f1dc8c1ba00e98ef77092e/5ff1a85664a2e10f370a6c02'
headers = {'User-Agent':'Mozilla/5.0'}
req = requests.get(url, headers = headers)
# print(req.status_code)

tree = html.fromstring(req.content)
# NetA = tree.xpath('//section[@id="sample-network-traffic"]/h2/text()')
# dns1 = tree.xpath('//section[@id="sample-network-traffic"]/div[@id="dns-requests"]/h3/text()')
# dnst = tree.xpath('//div[@id="dns-requests"]//table[@class="table table-striped small"]/thead/tr/th[contains(@class,"col-md")]/text()')
# dnst = tree.xpath('//div[@id="contacted-hosts"]/div[@class="table-scroll-container"]/table/thead/tr/th/text()') # hreader
dnst = tree.xpath('//div[@id="contacted-hosts"]/*/table/thead/tr/th/text()') # header ok
# print(dnst)
# ip = [i.text for i in tree.xpath('//div[@id="contacted-hosts"]/*/table/tbody/tr/td[1]')] # table o
# port_protocal= [i.text for i in tree.xpath('//div[@id="contacted-hosts"]/*/table/tbody/tr/td[2]')] # table ok
# associated_process = [i.text for i in tree.xpath('//*[@id="contacted-hosts"]/div/table/tbody/tr/td[3]')] # table ok


table = tree.xpath('//*[@id="contacted-hosts"]/div[2]/table/tbody/tr/td[1]/text()')
ip = [table[i].strip() for i in range(len(table))]
ips = []
for item in ip:
    if item !='':
        ips.append(item)
# print(ips) #ok
# print(len(ips)) #ok


d = tree.xpath('//*[@id="contacted-hosts"]/div[2]/table/tbody/tr/td[2]/a/text()')
d2=tree.xpath('//*[@id="contacted-hosts"]/div[2]/table/tbody/tr/td[2]/span/text()')
ports =[list(x) for x in zip(d,d2)]
# print(ports)
# print(len(ports))

d3 = tree.xpath('//*[@id="contacted-hosts"]/div[2]/table/tbody/tr/td[3]/span/text()')
# print(d3)
# print(len(d3))

details = tree.xpath('//*[@id="contacted-hosts"]/div[2]/table/tbody/tr/td[4]/text()') # table ok

details = [details[i].strip()  for i in range(len(details))]
countries = []
for item in details:
    if item != '':
        countries.append(item)
# print(countries) #ok
# print(len(countries))

mydata_table = [list(x) for x in zip(ips,ports,d3,countries)]
# print(mydata_table)

from tabulate import tabulate



print(tabulate(mydata_table, headers=dnst))
