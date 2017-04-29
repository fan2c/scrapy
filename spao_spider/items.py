# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpaoSpiderItem(scrapy.Item):
    product_code = scrapy.Field()
    product_name = scrapy.Field()
    product_category = scrapy.Field()
    product_color = scrapy.Field()
    original_price = scrapy.Field()
    discount_price = scrapy.Field()
    product_thumbnail_images = scrapy.Field()
    product_url = scrapy.Field()
    product_fabric = scrapy.Field()
    product_gender = scrapy.Field()
    created_at = scrapy.Field()
