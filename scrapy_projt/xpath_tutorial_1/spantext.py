from scrapy.selector import Selector

html ="""<span id="status_connectionStatus" style="font-family: rubikReg; color: rgb(255, 255, 255);">Connected</span>
"""


data = Selector(text=html)

print(data.css('span#status_connectionStatus::text').get())
