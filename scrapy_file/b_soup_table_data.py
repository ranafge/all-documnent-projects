from bs4 import BeautifulSoup
import requests

tabel = '''<tr><td valign="top"><img src="/icons/compressed.gif" alt="[   ]"></td><td><a href="wsp_120hr5km_latest.zip">wsp_120hr5km_latest.zip</a></td><td align="right">2020-11-19 21:24  </td><td align="right"> 15K</td><td>&nbsp;</td></tr>

<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="latest_wsp64knt120hr_5km.kmz">latest_wsp64knt120hr..&gt;</a></td><td align="right">2020-11-19 21:24  </td><td align="right">715 </td><td>&nbsp;</td></tr>

<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="latest_wsp50knt120hr_5km.kmz">latest_wsp50knt120hr..&gt;</a></td><td align="right">2020-11-19 21:24  </td><td align="right">1.9K</td><td>&nbsp;</td></tr>'''

soup = BeautifulSoup(tabel, 'lxml')
print(soup.prettify())
