# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field

class CrawlerEggheadItem(scrapy.Item):
    main_category = scrapy.Field() #subject
    sub_category = scrapy.Field() #programming language
    lecturer = scrapy.Field()