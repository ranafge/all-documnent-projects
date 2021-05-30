from scrapy.selector import Selector

html="""<parentList>
      <parent attr1="a11" attr2="a12">
        <child1>c11</child1>
        <child2>c12</child2>
        <child3>c13</child3>
        <child4>c14</child4>
        <child5>c15</child5>
      </parent>
      <parent attr1="a21" attr2="22">
        <child1>c21</child1>
        <child2>c22</child2>
        <child3>c23</child3>
        <child4>c24</child4>
        <child5>c25</child5>
      </parent>
</parentList>"""

data = Selector(text=html)
print(data.xpath("//parent/concat(@attr1,' ',child3/text())"))
