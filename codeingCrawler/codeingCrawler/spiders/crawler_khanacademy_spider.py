import scrapy
from ..items import CodeingCrawlerItem
import re

f1 = open("inputs\\khanacademyLinks.txt", 'r', encoding='UTF8')
khanacademyLinks = []
while True:
    line = f1.readline()
    if not line : break
    line = line[:-1]
    khanacademyLinks.append(line)
f1.close()

class crawler_khanacademy_Spider(scrapy.Spider):
    name = "khanacademy"  #spider 이름
    allowed_domains = ["https://ko.khanacademy.org/"]  #최상위 도메인

    def start_requests(self):
        for i in range(0, len(khanacademyLinks), 1):
        #for i in range(0, 3, 1):
            yield scrapy.Request(khanacademyLinks[i], self.parse_egghead)

    def parse_egghead(self, response):
        item = CodeingCrawlerItem()
        item['lectureName'] = response.xpath('//*[@data-test-id="unit-block-title"]/text()').extract()[0]
        item['price'] = 0 #check
        item['lectureLink'] = response.xpath('//head/link/@href').extract()[0]
        item['thumbnail'] = "unknown"
        item['level'] = 6  # 제공되지 않음
        item['lecturer'] = "unknown"
        item['siteIdx'] = 3  # kocw
        item['rating'] = 6 #제공하지 않음
        item['contents'] = response.xpath('//h2/a/text()').extract()
        item['category'] = 'unknown'
        item['subCategory'] = 'unknown'
        item['type'] = "on"  # online
        item['language'] = "en" #english
        item['totalDuration'] = 'unknown'
        item['numOfLectures'] = len(item['contents'])
        yield item