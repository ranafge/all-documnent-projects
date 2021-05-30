import scrapy
html = '''<html><div><span class="c1">Text1</span><br/>Text4<br/>Text5</div>
                <div><span class="c1">TextA</span><a href="...">TextD</a></div>
        </html>'''
# Text1|
# Text4
# Text5$
# TextA|TextD$
data = scrapy.Selector(text=html)
# print(data.xpath("string(concat(//div[1], '$'))").get())#Text1Text4Text5$
# print(data.xpath("string(//div[1])"))#Text1Text4Text5$
Text1=data.xpath("string(//div[1]/span[contains(@class, 'c1')])")#Text1
Text4=data.xpath("substring-before(substring-after(//div[1], 'Text1'), 'Text5')") #Text4
Text5=data.xpath("substring-after(substring-after(//div[1], 'Text1'),'Text4')") #Text5
TextA=data.xpath("//div[2]/span[contains(@class, 'c1')]/text()")#TextA
TextD=data.xpath("//div[2]/a/text()")#TextD
print(Text1, Text4, TextA, TextD)
# print(data.xpath("//div/span[contains(@class, 'c1')]/text()").get())#Text1
# print(data.xpath("concat(string(//div[1]/span[contains(@class, 'c1')]),' ',substring-before(substring-after(//div[1], 'Text1'), 'Text5'),' ',substring-after(substring-after(//div[1], 'Text1'),'Text4'),' ',//div[2]/span[contains(@class, 'c1')]/text())").getall())
print(data.xpath("concat(string(//div[1]/span[contains(@class, 'c1')]),'|', '\n',substring-before(substring-after(//div[1], 'Text1'), 'Text5'),'\n',substring-after(substring-after(//div[1], 'Text1'),'Text4'),'$', '\n',//div[2]/span[contains(@class, 'c1')]/text(),'|',//div[2]/a/text(),'$')").get())
