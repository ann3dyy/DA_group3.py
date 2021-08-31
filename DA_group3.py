
# imports used in the script
#import request is used for lab 10b, to ensure that we CAN do HTTP requests towards the website using python
#without request, we cannot send HTTP requests to the website for our script to work
#import unittest is required so that we can actually test whether our units and our softwware code works
import requests
import unittest

#performing get request
testing = "https://brickset.com/sets/year-2000"
t = requests.get(testing)
print(t.text)

#doing the okay status
print("Status Code: ")
print("\t *", t.status_code)
if t.status_code == 200:
    print("Translation: 200 = OK")

#getting the header
h = requests.head(testing)
print("HEADER:")
print("*******************************************")
for x in h.headers:
    print("\t *", x, ":", h.headers[x])
print("*******************************************")

#attempting the user-agent
headers = {
            "User-Agent": "Mobile"
}
testing2 = "http://httpbin.org/headers"
rh = requests.get(testing2, headers=headers)
print(rh.text)



#doing scrapy
#without import scrapy we cannot use the modules within it, such as spider
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
