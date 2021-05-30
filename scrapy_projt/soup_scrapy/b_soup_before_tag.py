import bs4 as bs
import urllib.request as url
import requests

source = url.urlopen('https://www.facebook.com/events/777016493046448/')
soup = bs.BeautifulSoup(source, 'html.parser')
print(soup.prettify())
result = soup.find('span', attrs={'class':'d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v hnhda86s jdix4yx3 hzawbc8m'}).text

print(result)
