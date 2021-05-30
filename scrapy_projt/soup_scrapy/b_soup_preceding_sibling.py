from bs4 import BeautifulSoup


html ="""<div class="nw-priceblock-container">

   <del class="

          nw-priceblock-amt

          nw-priceblock-mrp

          is-having-discount

          ">Rs. 699 </del>

   <span class="

          nw-priceblock-amt

          nw-priceblock-sellingprice

          is-having-discount

          ">Rs. 489 </span>

   <span class="nw-priceblock-discount is-having-discount"> (30% Off)</span>

</div>"""

soup = BeautifulSoup(html, 'html.parser')

# find parent class
# print(soup.find('div', {'class': 'nw-priceblock-container'}))
parent_clsss = soup.find('div', {'class': 'nw-priceblock-container'})

# print(parent_clsss.find('span', {'class':'nw-priceblock-discount is-having-discount'}).text)
print(parent_clsss.find('span', {'class':'nw-priceblock-discount is-having-discount'}).find_previous('span').text)
