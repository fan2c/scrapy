# -*- coding: utf-8 -*-
import os
import re
import datetime
import logging
from scrapy import Spider
from scrapy.http import Request
from scrapy.http import FormRequest

def parse_number(string):
    return re.findall(r'\d+',string)[0]

class GoodsSpider(Spider):
    logging.basicConfig(filename='log.txt',
                        format='%(levelname)s: %(message)s',
                        level=logging.INFO)

    name = 'goods'
    allowed_domains = ['spao.elandmall.com']
    start_urls = ['http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1607300073',
                  'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1607300075',
                  'http://spao.elandmall.com/dispctg/initDispCtg.action?disp_ctg_no=1607300070']

    # parse category number
    def parse(self, response):

        disp_ctg_string = response.xpath('//*[@class="lnb_cate01"]/ul/li/a[@href="#none"]/@onclick').extract()
        for ctg_no in disp_ctg_string:
            ctg_no = parse_number(ctg_no)
            url = 'http://spao.elandmall.com/dispctg/initDispCtg.action'
            absolute_url = response.urljoin(url)
            formdata = {"listOnly":"Y",
                        "kwd":"",
                        "disp_ctg_no":ctg_no,
                        "category_1depth":"",
                        "category_2depth":ctg_no,
                        "category_3depth":"",
                        "category_4depth":"",
                        "category_5depth":"null",
                        "category_6depth":"null",
                        "brand_no":"",
                        "vend_no":"",
                        "material_info":"",
                        "size_info":"",
                        "deliCostFreeYn":"",
                        "setDicountYn":"",
                        "giftYn":"",
                        "oneMoreYn":"",
                        "discountYn":"",
                        "min_price":"",
                        "max_price":"",
                        "color_info":"",
                        "reSrch":"",
                        "page_idx":"1",
                        "pageSize":"500",
                        "srchFd":"null",
                        "sort":"1",
                        "listType":"image",
                        "applyStartDate":"",
                        "applyEndDate":"",
                        "dispStartDate":"",
                        "dispEndDate":"",
                        "newGoodsStartDate":"",
                        "newGoodsEndDate":"",
                        "mall_no":"0000037"
                        }
            # print(formdata)
            yield FormRequest(absolute_url, callback=self.parse_goods_number,formdata=formdata)

    # parse gooods number
    def parse_goods_number(self, response):

        goods_list_string = response.xpath('//li/a[@href="javascript:;"]/@onclick').extract()
        for goods_no in goods_list_string:
            goods_no = parse_number(goods_no)
            url = 'http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=' + goods_no
            absolute_url = response.urljoin(url)
            yield Request(absolute_url, callback=self.parse_goods)
            # yield Request(absolute_url, dont_filter=True, callback=self.parse_goods)

    # parse gooods detail
    def parse_goods(self, response):

        product_code = response.xpath('//*[@name="goods_no"]/@value').extract_first()
        product_name = response.xpath('//*[@name="goods_nm"]/@value').extract_first()
        product_category = response.xpath('//*[@selected="selected"]/text()').extract()
        product_table = response.xpath('//table/tbody/tr/td/text()').extract()

        product_color = product_table[1].split(',')
        product_color = list(product_color)

        product_fabric = product_table[0]

        discount_price = response.xpath('//*[@id="detailform"]/div/div/ul[1]/li/span[2]/strong/text()').extract_first()

        if discount_price:
            original_price = response.xpath('//*[@id="detailform"]/div/div/ul[1]/li/span[1]/text()').extract_first()
            original_price = re.findall(r"\d+,\d+",original_price)[0]
        else:
            original_price = response.xpath('//*[@id="detailform"]/div/div/ul[1]/li/span/strong/text()').extract_first()

        product_thumbnail_images = response.xpath('//*[@id="d_elevate_img"]/@src').extract_first()
        product_thumbnail_images = product_thumbnail_images.replace("//","http://")
        product_url = 'http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=' + product_code

        if 'WOMEN' in product_category:
            product_gender = 'female'
        elif 'MEN' in product_category:
            product_gender = 'male'
        else:
            product_gender = None

        created_at = datetime.datetime.now().isoformat()

        yield { 'product_code': product_code,
                'product_name': product_name,
                'product_category': product_category,
                'product_color': product_color,
                'original_price': original_price,
                'discount_price': discount_price,
                'product_thumbnail_images': product_thumbnail_images,
                'product_url': product_url,
                'product_fabric': product_fabric,
                'product_gender': product_gender,
                'created_at': created_at
                }
