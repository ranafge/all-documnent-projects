# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import TakeFirst, MapCompose, Join
class REItem(scrapy.Item):
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, lambda value: float(value.replace("\n", "").replace(" ", "").replace(",", ".")))
    )
    size = scrapy.Field(
        input_processor=MapCompose(remove_tags, lambda value: float(value.replace("\n", "").replace(" ", "").replace(",", ".")))
    )
    rooms = scrapy.Field(
        input_processor=MapCompose(remove_tags, lambda value: int(value.replace("&gt;", "").replace("\n", "").replace(" ", "")))
    )
