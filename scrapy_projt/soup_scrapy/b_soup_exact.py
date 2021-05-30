from bs4 import BeautifulSoup
html ="""<span class="market_table_value normal_price">
                    Starting at:<br/>
<span class="normal_price" data-currency="1" data-price="69">$0.69 USD</span>
<span class="sale_price">$0.66 USD</span>
</span>"""


soup = BeautifulSoup(html, 'html.parser')

price = soup.select_one('span[data-currency^="1"]').get_text()
print(price) #$0.69 USD

