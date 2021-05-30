import scrapy
html="""<form class="variants" action="/cart">
    <a class="thumb fancybox image_outer" href="products/apple-iphone-5s-16gb-black--space-gray-chernyj" data-fancybox-group="gallery5">
        <img src="http://first-store.ru/files/products/iphone%205S%20black_1.100x112.jpg?16ef5c4132fc88594851f92ccc2f3437" alt="Apple iPhone 5s 16GB Black &amp; Space Gray (Чёрный)" title="Apple iPhone 5s 16GB Black &amp; Space Gray (Чёрный)">
    </a>
    <h1>
        <a class="name_mark" data-product="1075" href="products/apple-iphone-5s-16gb-black--space-gray-chernyj">Apple iPhone 5s 16GB Black &amp; Space Gray (Чёрный)</a>
    </h1>
    <span class="price price_mark price_value">26 990&nbsp;<span class="currency">руб</span>
        <input id="variants_2927" name="variant" value="2927" type="radio" class="variant_radiobutton" checked="" style="display:none;">
        <input class="button buy buy_button buy_button_catalog" type="submit" value="Купить" data-result-text="Добавлено">
    </span>     
</form>"""

data = scrapy.Selector(text=html)
print(data.xpath("span[contains(concat(' ', normalize-space(@class), ' '), ' price ')]"))
