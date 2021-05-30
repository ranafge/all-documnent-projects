from scrapy.selector import Selector

html = """<item>
    <element1>el1</element1>
    <element2>el2</element2>
    <element3>el3</element3>
    <element4>
        <subEl1>subel1a</subEl1>
        <subEl2>subel2a</subEl2>
    </element4>
    <element4>
        <subEl1>subel1b</subEl1>
        <subEl2>subel2b</subEl2>
    </element4>
</item>"""


data = Selector(text=html)

print(data.get())
data1 = data.xpath("//p/span[1]/text()").get()
data2 = data.xpath("//p/span[2]/text()").get()
data3 = data.xpath("//p/span[3]/text()").get()
data4 = data.xpath("//p/span[4]/text()").get()
print(data1)
print(data2)
print(data3)
print(data4)
print('Now it is concating strings: ')
print(data.xpath("concat(//p/span[1]/text(),' ,', //p/span[2]/text(), ' ,',//p/span[3]/text(), ', ', //p/span[4]/text() )").get())
print(data.xpath("string-join('//element4', ' ')"))

