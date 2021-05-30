import requests
from bs4 import BeautifulSoup

text = '''<span class="
hp_address_subtitle
js-hp_address_subtitle
jq_tooltip
" rel="14" data-source="top_link" data-coords="," data-component="tooltip" data-tooltip-text="
<p>Ubicación <strong>excelente</strong>, ¡puntuada con 9,3/10! <small>(puntaje basado en <strong>Más recomendado</strong> comentarios)</small></p>
<p>Valorado por las personas <strong>después de hospedarse en</strong> el Hotel Panamericano Buenos Aires.</p>
" data-tooltip-animation="false" tabindex="0" data-bbox="-58.4028009366937,-34.6199039159457,-58.3590682554297,-34.5839730827995" data-node_tt_id="location_score_tooltip" data-width="350" title="" aria-describedby="tooltip-1">
Carlos Pellegrini 551, C1009ABK Buenos Aires, Argentina
</span>'''

soup = BeautifulSoup(text, 'lxml')
print(soup.prettify())

for ele in soup.find_all(text=True):
    print(ele)


page = requests.get("https://www.booking.com/hotel/ar/panamericano-buenos-aires.es-ar.html")

soup = BeautifulSoup(page.content, 'lxml')

output = soup.find('span', {'class': 'hp_address_subtitle'})
print(output.text)

