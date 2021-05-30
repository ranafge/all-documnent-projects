import scrapy
html ="""<div class="group">
    <ul class="smallList">
        <li><strong>Date</strong>
        13.06.2019
        </li>
        <li>after1</li>
        <li>after2</li>
    </ul>
</div>"""
data = scrapy.Selector(text=html)
print(data.xpath("substring-after(//div[@class='group']/ul/li[1],'Date')").get())
print(data.xpath("substring-after(//div[@class='group']/ul/li[1], 'Date')").getall())
