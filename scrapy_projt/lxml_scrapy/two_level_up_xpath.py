from lxml import etree
html ="""<div class="search_hit">
    <span prop="name">Richard Winchester</span>
    <span prop="company">Kodak</span>
    <span prop="street">Arlington Road 1</span>
</div>
<div class="search_hit">
    <span prop="name">Ted Mosby</span>
    <span prop="company">HP</span>
    <span prop="street">Arlington Road 2</span>
</div>
"""
root = etree.fromstring(html)
