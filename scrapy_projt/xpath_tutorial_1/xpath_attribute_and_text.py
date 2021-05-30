from scrapy.selector import Selector

html ="""<RootNode>
  <FirstChild>
    <Element attribute1="abc" attribute2="xyz">Data</Element>
  <FirstChild>
</RootNode>"""

data = Selector(text=html)
print(data.get())
print(data.xpath("//*/element[@attribute1='abc' and @attribute2='xyz' and text()='Data']").get())
