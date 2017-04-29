# Goods Bot

This is a Scrapy project to scrape goods information from http://spao.elandmall.com .

This project is only meant for practice purposes.

## Extracted data

This project extracts goods information, The extracted data looks like this sample:

    {
        "_id" : ObjectId("5900a80cfd338d31b4af1681"),
        "original_price" : "39,900",
        "product_category" : [ 
            "WOMEN", 
            "SHIRT", 
            "체크/패턴 셔츠"
        ],
        "discount_price" : null,
        "product_color" : [ 
            "그레이", 
            " 네이비"
        ],
        "product_gender" : "female",
        "product_code" : "1704178817",
        "product_fabric" : "면 98%, 폴리우레탄 2%",
        "product_url" : "http://spao.elandmall.com/goods/initGoodsDetail.action?goods_no=1704178817",
        "created_at" : "2017-04-26T23:00:44.325687",
        "product_thumbnail_images" : "http://www.elandmall.com/upload/prd/img/817/600/1704178817_0000001.jpg",
        "product_name" : "(#)소매 배색 와이드 셔츠"
    }

## Running the spiders

You can run a spider using the scrapy crawl command, such as:

$ scrapy crawl goods

It will be save the scraped data to "spao_data_utf8.json" file, also save to mongDB at the same time.

