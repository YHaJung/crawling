"""
Created on Wed Jan 9 13:09 2021

@author: hj99y
"""

import scrapy
from ..items import CodeingCrawlerItem
import re

f1 = open("inputs\\kmoocLinks.txt", 'r', encoding='UTF8')
kmoocLinks = []
while True:
    line = f1.readline()
    if not line : break
    line = line[:-1]
    kmoocLinks.append(line)
f1.close()

class crawler_kmooc_Spider(scrapy.Spider):
    name = "kmooc"  #spider 이름
    allowed_domains = ["http://www.kmooc.kr/"]  #최상위 도메인

    def start_requests(self):
        for i in range(0, len(kmoocLinks), 1):
            #for i in range(0, 3, 1):
            yield scrapy.Request(kmoocLinks[i], self.parse_egghead)

    def parse_egghead(self, response):
        item = CodeingCrawlerItem()
        item['lectureName'] = response.xpath('//*[@class="heading-group"]/h1/text()').extract()[0].split('\n')[1].lstrip()
        item['price'] = 0
        item['lectureLink'] = response.xpath('//*[@id="clipboard-temp"]/@value').extract()[0]
        item['thumbnail'] = 'http://www.kmooc.kr'+response.xpath('//*[@class="hero"]/img/@src').extract()[0]
        item['level'] = 6 #제공되지 않음
        item['lecturer'] = response.xpath('//*[@class="staff_descript"]/dl/dt').extract()[0]
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
        item['lecturer'] = hangul.sub('', item['lecturer']).strip().split()[0]
        item['siteIdx'] = 16  # kmooc
        rating = response.xpath('//*[@class="faq-container"]/label/div/p/text()').extract()
        if rating:
            item['rating'] = float(rating[0].split('(')[1].split(')')[0])
        else:
            item['rating'] = 0 #평점 없음

        item['contents'] = ''
        contents = response.xpath('//tr/td[2]/p/span/text()').extract()
        if contents:
            contents = contents
        else:
            contents = response.xpath('//tr/td[2]/text()').extract()
        for content in contents:
            item['contents'] += content.lstrip()
        item['contents'] = re.sub('[-=.#/?:$\n}]', '', item['contents'])
        item['category'] = 'unknown'
        item['subCategory'] = 'unknown'
        item['type'] = "on"  # online
        item['language'] = "ko" #korean
        time = response.xpath('//ol/li[4]/div/span/text()').extract()[1].strip()
        hour = int(time[1:3])
        minute = int(time[6:8])
        item['totalDuration'] = hour*60 + minute
        item['numOfLectures'] = int(response.xpath('//ol/li[3]/div/span/span/text()').extract()[0][0:2])  #주차 수로 대체
        yield item