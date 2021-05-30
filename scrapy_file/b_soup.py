from bs4 import BeautifulSoup

html = """
<div class="profile-info__address" itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress">
            <img src="/Content/images/icons/location-pin.svg" class="icon-left">
            1000 Bruxelles<br>Rue de Laeken 160
        </div>
"""
soup = BeautifulSoup(html,features='lxml')
address_container = [item.strip() for item in soup.select_one("[itemprop='address']") if item.string]
print(address_container)
for i in address_container:
    print(i.strip())
