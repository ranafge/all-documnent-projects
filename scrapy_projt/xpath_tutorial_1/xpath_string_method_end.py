import scrapy
html = '''<div id="qa-case"> 
<time itemprop="datePublished" datetime="2015-01-12T02:41:00Z"></time>
</div'''
html2="""<div id="RF4FOEQ3OPBEX" data-hook="review" class="a-section review aok-relative">
   <div data-hook="review-collapsed" aria-expanded="false" class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content">
      <span> 
             Text line1. 
             <br>
             Text line2. 
       </span>
       </div></div>"""
data = scrapy.Selector(text=html2)
print(data.xpath('//div[@data-hook="review"]//div[@data-hook="review-collapsed"]/span/text()').getall())
print(data.xpath('string(//div[@data-hook="review"]//div[@data-hook="review-collapsed"]/span/text())').getall())
