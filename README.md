GoodsBot

This is a Scrapy project to scrape goods information from http://spao.elandmall.com .

This project is only meant for practice purposes.

Extracted data

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

Spiders

This project contains two spiders and you can list them using the list command:

  INFO: Dumping Scrapy stats:
  {'downloader/request_bytes': 4225738,
   'downloader/request_count': 1455,
   'downloader/request_method_count/GET': 1435,
   'downloader/request_method_count/POST': 20,
   'downloader/response_bytes': 169428001,
   'downloader/response_count': 1455,
   'downloader/response_status_count/200': 1455,
   'dupefilter/filtered': 458,
   'finish_reason': 'finished',
   'finish_time': datetime.datetime(2017, 4, 26, 14, 2, 59, 125348),
   'item_scraped_count': 1432,
   'log_count/DEBUG': 2889,
   'log_count/INFO': 9,
   'request_depth_max': 2,
   'response_received_count': 1455,
   'scheduler/dequeued': 1455,
   'scheduler/dequeued/memory': 1455,
   'scheduler/enqueued': 1455,
   'scheduler/enqueued/memory': 1455,
   'start_time': datetime.datetime(2017, 4, 26, 14, 0, 40, 167947)}
  INFO: Spider closed (finished)

Running the spiders

You can run a spider using the scrapy crawl command, such as:

$ scrapy crawl goods

It will be save the scraped data to "spao_data_utf8.json" file, also save to mongDB at the same time.

