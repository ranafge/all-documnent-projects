import scrapy

html = """<table>
    <th>Abbreviation</th>
    <tr>
        <td>
            <span><u>General</u><br/></span>
            My Text <!--The text i want to get-->
            <br/><u>Def</u>
            Some other Text
       </td>
</table>"""

data = scrapy.Selector(text=html)
print(data.xpath('//span[u]/following-sibling::text()[1][normalize-space(text()="My Text")]').get())
