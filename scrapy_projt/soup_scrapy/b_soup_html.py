from bs4 import BeautifulSoup

html = '''<div class="_1hVBfR">
   <span class="row _1kkfO3 BqOr_g">Google Nest Mini (2nd Gen) with Google A...</span>
   <div class="row _65ZkAB">
      <span class="_3dOR_a">
      <span class="_65ZkAB">Color: </span>
      <span class="-igymY">Black</span></span>
      <span class="_3dOR_a"></span>
   </div>
   <div class="row _65ZkAB">
      <span class="_65ZkAB _1uABhR">Seller: </span>
      <span class="-igymY">Net Seller</span>
   </div>
</div>'''

soup = BeautifulSoup(html, 'lxml')

res = soup.find_all('span', {'class': '-igymY'})[1]

print(res.text)

res = soup.find_all('span', {'class': '-igymY'})

print([t.text  for t in res if t.text == 'Net Seller'])
