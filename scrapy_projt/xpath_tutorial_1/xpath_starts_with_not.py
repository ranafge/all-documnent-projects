import scrapy
html = """<people>
  <person displayName="first1 last2" firstName="first1" lastName="last1" preferredName="preferred1" />
  <person displayName="preferred2 last2" firstName="first2" lastName="last2" preferredName="preferred2" />
</people>"""


data = scrapy.Selector(text=html)

print(data.xpath("//person[not(starts-with(@displayName, @preferredName))]"))
