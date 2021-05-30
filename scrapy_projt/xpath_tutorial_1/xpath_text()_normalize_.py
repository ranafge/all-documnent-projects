from scrapy.selector import Selector

html="""<p>
    <br>foo<strong>this foo</strong>
    
    <br>bar<strong>this bar</strong>
    
    <br>baz<strong>this baz</strong>
    
    <br>qux<strong>this qux</strong>
    </p>
"""
data = Selector(text=html)
print(data.xpath('//p/text()[contains(.,"baz")]/following-sibling::strong[1]/text()').get())
print(data.xpath('//p/text()[normalize-space(.)= "baz"]/following-sibling::strong[2]/text()').get())

