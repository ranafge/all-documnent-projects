import scrapy
html="""<html>
  <h3>Title T31</h3>
    <a31/>
    <b31/>
  <h3>Title T32</h3>
    <a32/>
    <b32/>
  <h3>Title T33</h3>
    <a33/>
    <b33/>
  <h3>Title T34</h3>
    <a34/>
    <b34/>
  <h3>Title T35</h3>
</html>"""

data = scrapy.Selector(text=html)
print(data.getall())
print(data.xpath('//*/h3/following-sibling::node()[not(self::h3)][count(preceding-sibling::h3)=2]').getall())
