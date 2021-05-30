from bs4 import BeautifulSoup

html ="""<div><strike class='original-price'> 150 </strike><p class='sale-price'> 120 </p></div>"""
soup = BeautifulSoup(html, 'html.parser')
sale_price = soup.find('p', class_='sale-price').text
print(sale_price)
original_price = soup.find('strike', class_='original-price').text
print(original_price)
