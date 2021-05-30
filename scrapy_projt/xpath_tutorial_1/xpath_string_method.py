from scrapy.selector import Selector
from bs4 import BeautifulSoup
import requests

html ="""<parents name='Parents'>
          <Parent id='1' name='Parent_1'>
            <Children name='Children'>
              <child name='Child_2' id='2'>child2_Parent_1x<strong>child2_strong_Parent_1</strong></child>
              <child name='Child_4' id='4'>child4_Parent_1</child>
              <child name='Child_1' id='3'>child1_Parent_1</child>
              <child name='Child_3' id='1'>child3_Parent_1</child>
            </Children>
          </Parent>
</parents>
<p>Whatever you want type <strong>here is great</strong></p>

"""

data = Selector(text=html)
# print(data.get())
# print(data.xpath('//parents[@name="Parents"]/parent/children/child[@name="Child_2"]/text()').getall())
# print(data.xpath('string(//parents[@name="Parents"]/Children[@name="Children"]//child/text())').getall())
print(data.xpath('string(//p)').getall())
print(data.xpath("concat(//p/text()[1],//p//text()[2])").getall())
print(data.xpath('string(//p[.="Whatever you want type "])').get())
