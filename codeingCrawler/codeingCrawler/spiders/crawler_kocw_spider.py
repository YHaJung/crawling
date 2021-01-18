import scrapy
from ..items import CodeingCrawlerItem
import re

f1 = open("inputs\\kocwLinks.txt", 'r', encoding='UTF8')
kocwLinks = []
while True:
    line = f1.readline()
    if not line : break
    line = line[:-1]
    kocwLinks.append(line)
f1.close()

class crawler_kmocw_Spider(scrapy.Spider):
    name = "kocw"  #spider 이름
    allowed_domains = ["http://kocw.or.kr/"]  #최상위 도메인

    def start_requests(self):
        for i in range(0, len(kocwLinks), 1):
            #for i in range(0, 3, 1):
            yield scrapy.Request(kocwLinks[i], self.parse_egghead)

    def parse_egghead(self, response):
        item = CodeingCrawlerItem()
        item['lectureName'] = response.xpath('//*[@class="detailTitle"]/a/text()').extract()[0]
        item['price'] = 0
        item['lectureLink'] = response.xpath('//*[@class="detailTitle"]/a/@href').extract()[0]
        try:
            item['thumbnail'] = 'http://www.kocw.net'+response.xpath('//*[@alt="강의사진"]/@src').extract()[0]
        except:
            item['thumbnail'] = 'http://www.kocw.net/home/images/common/noImg.gif'
        item['level'] = 6  # 제공되지 않음
        item['lecturer'] = response.xpath('//ul[@class="detailTitInfo"]/li[2]/text()').extract()[0]
        item['siteIdx'] = 15  # kocw
        try:
            item['rating'] = float(response.xpath('//*[@class="detailViewStyle01"]/ul[2]/li[2]/dl/dd/text()').extract()[0].split('/')[0])
        except:
            item['rating'] = 0
        item['contents'] = response.xpath('//*[@class="tbType01"]/tbody/tr/td[4]/text()').extract()
        item['category'] = 'unknown'
        item['subCategory'] = 'unknown'
        item['type'] = "on"  # online
        item['language'] = "ko" #korean 다시 확인
        item['totalDuration'] = 'unknown'
        item['numOfLectures'] = len(item['contents'])
        yield item