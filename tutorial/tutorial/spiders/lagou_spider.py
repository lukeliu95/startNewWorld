#第一个爬虫例子
import scrapy
import io

class DmozSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = [
        "https://www.lagou.com/jobs/list_PHP?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
        "https://www.lagou.com/zhaopin/PHP/?labelWords=label"
    ]

    def parse(self, response):
        filename = "lagou.txt"
        with open(filename, 'wb') as f:
            f.write(response.body)
