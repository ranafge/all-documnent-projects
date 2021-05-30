import re
from bs4 import BeautifulSoup

html_doc = """#Query:[<div class="price">
<span class="price-currency">$</span>
<label for="low-price" hidden="">Low Price</label>
<input class="price-filter" data-val="true" data-val-number="The field LowPrice must be a number." data-val-required="The LowPrice field is required." id="low-price" name="SearchCriteria.LowPrice" placeholder="Min" type="text" value="0.00">
<span class="price-currency">$</span>
<label for="high-price" hidden="">Low Price</label>
<input class="price-filter" data-val="true" data-val-number="The field HighPrice must be a number." data-val-required="The HighPrice field is required." id="high-price" name="SearchCriteria.HighPrice" placeholder="Max" type="text" value="999999.00">
</input></input></div>, <div class="price">
$1,001.00                                    </div>]"""

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.find('div', class_='price').find_all_next('div')[0].text)
# print(soup.prettify())
prices = soup.find_all('div', class_='price', text=re.compile('\d+'))
print(prices[0].text)

