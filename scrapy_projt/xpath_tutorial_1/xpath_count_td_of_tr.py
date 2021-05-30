import scrapy

html ="""<table>
  <tr>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  <tr>
     <td></td>
  </tr>
  <tr>
     <td></td>
     <td></td>
     <td></td>
     <p></p>
   </tr>
  <tr>
     <td></td>
     <p></p>
  </tr>
</table>"""

data = scrapy.Selector(text=html)

print(data.xpath('//tr[count(td) = 3]'))
