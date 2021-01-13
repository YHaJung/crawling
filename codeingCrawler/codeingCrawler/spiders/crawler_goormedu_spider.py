# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:56:09 2021

@author: hj99y
"""
import scrapy
from importlib import reload
from scrapy.spiders import Spider
from ..items import CodeingCrawlerItem
from datetime import datetime

from scrapy.http import Request
from scrapy.selector import Selector

f1 = open("inputs\\goormeduLinks.txt", 'r', encoding='UTF8')
goormeduLinks = []
while True:
    line = f1.readline()
    if not line : break
    line = line[:-1]
    goormeduLinks.append(line)
f1.close()

class crawler_goormedu_Spider(scrapy.Spider):
    name = "goormedu"  #spider 이름
    allowed_domains = ["edu.goorm.io"]  #최상위 도메인

    def start_requests(self):
        for i in range(0, len(goormeduLinks), 1):
            #for i in range(20, 40, 1):
            yield scrapy.Request(goormeduLinks[i], self.parse_egghead)

    def parse_egghead(self, response):
        item = CodeingCrawlerItem()
        item['lectureName'] = response.xpath('//h1/text()').extract()[0]
        price = response.xpath('//*[@data-mkt-id="edu_lecture_div_lecturePrice"]/text()').extract()
        if price:
            item['price'] = 0
        else:
            item['price'] = response.xpath('//*[@data-mkt-id="edu_lecture_div_lecturePrice"]/span/text()').extract()[0]

        item['lectureLink'] = response.xpath('/html/head/link[@rel="canonical"]/@href').extract()[0]
        item['thumbnail'] = response.xpath('//*[@data-mkt-id="edu_lectureDetail_img_thumbnail"]/@style').extract()[0].split("url(")[1].split(")")[0]
        item['level'] = response.xpath('//*[@class="_1dUlQs container-fluid"]/div[2]/div[2]/span/text()').extract()[0]
        item['lecturer'] = response.xpath('//*[@class="card-body"]/div[1]/div[2]/div[1]/text()').extract()[0]
        item['siteIdx'] = 19  # goormedu
        item['rating'] = float(response.xpath('//*[@class="_1dUlQs container-fluid"]/div[1]/div[2]/div/div/span/text()').extract()[0])

        # 목차 list를 string으로
        item['contents'] = ''
        contents1 = response.xpath('//ul[contains(@class, "list-group")]/li/div[2]/text()[1]').extract()
        contents2 = response.xpath('//ul[contains(@class, "list-group")]/div/div/div[2]/text()').extract()
        item['contents'] = contents1 + contents2
        item['category'] = response.xpath('//div[contains(@class, "card-body")]/div/div[2]/div[2]/text()').extract()[0]
        item['subCategory'] = response.xpath('//div[contains(@class, "card-body")]/div/div[3]/div[2]/text()').extract()[0]
        item['type'] = "on"  # online
        item['language'] = "ko" #korean
        item['totalDuration'] = "unknown"
        item['numOfLectures'] = len(contents2)
        print(contents1)
        print(contents2)
        yield item