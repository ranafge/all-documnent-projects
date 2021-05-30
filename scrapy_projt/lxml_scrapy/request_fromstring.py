from lxml import html
import requests
for e in range(0,1):
    page = requests.get("https://www.roblox.com/catalog/138932314/Dominus-Aureus")
    hTml = html.fromstring(page.text)
    print(hTml)
    clean_hTml = hTml.xpath("//div[@class='icon-text-wrapper clearfix icon-robux-price-container']/span/text()")
print(clean_hTml)


















