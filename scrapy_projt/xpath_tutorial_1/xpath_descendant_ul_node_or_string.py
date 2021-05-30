import scrapy

html = """<ul>
    <li class="type">Industry</li> 
    <li><a href="/store/Browse/?N=355+361+4294855087">Automotive</a></li>                            
    <li><a href="/store/Browse/?N=355+361+4294855065">Parts </a></li>                                
    <li>Tires</li>                  
</ul>"""

data = scrapy.Selector(text=html)
print(data.xpath('//ul/descendant::*/text()').getall()) #ok
