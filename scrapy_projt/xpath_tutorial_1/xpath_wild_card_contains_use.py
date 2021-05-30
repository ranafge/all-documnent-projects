from scrapy.selector import Selector
from bs4 import BeautifulSoup
import requests

html ="""<parents name='Parents'>
          <Parent id='1' name='Parent_1'>
            <Children name='Children'>
              <child name='Child_2' id='2'>child2_Parent_1x <strong> child2_strong_Parent_1xsx</strong></child>
              <child name='Child_4' id='4'>child4_Parent_1</child>
              <child name='Child_1' id='3'>child1_Parent_1</child>
              <child name='Child_3' id='1'>child3_Parent_1</child>
            </Children>
          </Parent>
          <things>
            <stuff>here are some things <yep>blue</yep> and here are some more things</stuff>
          </things>
</parents>"""
data = Selector(text=html)
result = data.xpath('string(//*[@*[contains(., "Child")]])').getall()
print(result)

string_data = data.xpath("string(//things/stuff)").getall()
print(string_data)
