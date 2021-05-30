from bs4 import BeautifulSoup

sample_html = """
<tr><td valign="top"><img src="/icons/compressed.gif" alt="[   ]"></td><td><a href="wsp_120hr5km_latest.zip">wsp_120hr5km_latest.zip</a></td><td align="right">2020-11-19 21:24  </td><td align="right"> 15K</td><td>&nbsp;</td></tr>

<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="latest_wsp64knt120hr_5km.kmz">latest_wsp64knt120hr..&gt;</a></td><td align="right">2020-11-19 21:24  </td><td align="right">715 </td><td>&nbsp;</td></tr>

<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="latest_wsp50knt120hr_5km.kmz">latest_wsp50knt120hr..&gt;</a></td><td align="right">2020-11-19 21:24  </td><td align="right">1.9K</td><td>&nbsp;</td></tr"""

soup = BeautifulSoup(sample_html, "html.parser")
print(soup.prettify())
myanchor = [x.find('a')['href'] for x in soup.find_all('td') if x.find('a')]
print("myanchor", myanchor)
mydates =[d.getText(strip=True) for d in soup.find_all('td', {'align': 'right'}) if "2020" in d.getText(strip=True)]
print(mydates)
for x in zip(myanchor, mydates):
    print(*x)

anchors = [a.find("a")["href"] for a in soup.find_all("td") if a.find("a")]
dates = [
    d.getText(strip=True) for d in soup.find_all("td", {"align": "right"})
    if "2020" in d.getText()
]

for item in zip(anchors, dates):
    print(*item)
