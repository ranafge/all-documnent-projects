import requests
from bs4 import BeautifulSoup
headers = {
    "Referer": "https://app.powerbigov.us/view?r=eyJrIjoiMTllMTM1ODctNjgyZi00NTNhLTlkYjAtOGE3MmZkODA0ODYxIiwidCI6IjIyZDVjMmNmLWNlM2UtNDQzZC05YTdmLWRmY2MwMjMxZjczZiJ9&navContentPaneEnabled=false&filterPaneEnabled=false",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

result = requests.get("https://data.sfgov.org/stories/s/COVID-19-Cases-and-Deaths/dak2-gvuj/", headers=headers)

src = result.content

soup = BeautifulSoup(src, 'lxml')

elements = soup.select('tspan', {'class': 'value'})
print(elements)
# print("\n")
# not work
