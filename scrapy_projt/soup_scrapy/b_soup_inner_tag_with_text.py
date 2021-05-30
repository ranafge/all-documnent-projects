from bs4 import BeautifulSoup
html="""
<div class="field required type-thumb_gallery" data-option_id="77502"></div>
<div class="field required type-product" data-option_id="77503"></div>
<div class="field required type-thumb_gallery" data-option_id="77504"></div>
<div class="field required type-product" data-option_id="77505"></div>
<div class="field required type-product" data-option_id="77506" style="display: none;"></div>

</div>"""

soup = BeautifulSoup(html, 'lxml')
print(soup.select('div:not(div[style="display: none;"])'))

