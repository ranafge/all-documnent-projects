from scrapy import Selector

html = '''<Home>
    <Addr>
        <Street>ABC</Street>
        <Number>5</Number>
        <Comment>BLAH BLAH BLAH <br/><br/>ABC</Comment>
    </Addr>
</Home>
<bla>
 <a prop="Foo1"/>
 <a prop="Foo2"/>
 <a prop="3Foo"/>
 <a prop="Bar"/>
</bla>
'''

data = Selector(text=html)
print(data.xpath('//text()[contains(., "ABC")]').get()) # ABC
print(data.xpath('//*[contains(., "ABC")]'))
print(data.xpath('//a[contains(@prop, "Foo")]').getall())

