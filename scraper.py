import scrapy
from scrapy.http.request import Request


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ["https://brickset.com/sets/year-2000"]

    def start_requests(self):
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; vc:48.0) Gecko/20100101 Firefox/48.0"}
        for url in self.start_urls:
            yield Request (url, headers=headers)



    def parse(self, response):
        SET_SELECTOR = ".set"
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = "h1 ::text"
            yield{
                "name": brickset.css(NAME_SELECTOR).extract_first(),
            }
