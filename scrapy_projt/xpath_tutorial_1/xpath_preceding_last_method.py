from scrapy.selector import Selector

html="""<table width="240" border="0" cellpadding="0" cellspacing="0" class="leftnav">
  <tr class="leftnav">
    <th>Type1</th>
  </tr>
  <tr class="leftnav">
    <td><a href="/mic/1.htm">2013</a></td>
  </tr>
  <tr class="leftnav">
    <td><a href="/mic/2.htm">2012</a></td>
  </tr>
  <tr class="leftnav">
    <td><a href="/mic/3.htm">2011</a></td>
  </tr>
  <tr class="leftnav">
    <td><a href="/mic/4.htm">2010</a></td>
  </tr>
   <tr class="leftnav">
    <th>Type2</th>
  </tr>
   <tr class="leftnav">
     <td><a href="/mic/5.htm">2013</a></td>
   </tr>
</table>"""

data = Selector(text=html)

print(data.xpath('//tr[(preceding-sibling::tr/th)[last()]="Type2"]/td/a/text()').get())
