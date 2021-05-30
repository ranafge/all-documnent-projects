from bs4 import BeautifulSoup
import re
import requests
url ="http://www.reading.ac.uk/ready-to-study/study/subject-area/modern-languages-and-european-studies-ug/ba-spanish-and-history.aspx"
res = requests.get(url).text
soup = BeautifulSoup(res, 'lxml')

course_data ={}
fees_div = soup.find('div', class_='Fees hiddenContent pad-around-large tabcontent').find_all('p')
print(fees_div)
for d in fees_div:
    print(d.text.split('students: ', 1)[-1].strip('* | '))


    # course_data['Fees'] = fees_list
    # print('fees : ', fees_list)
