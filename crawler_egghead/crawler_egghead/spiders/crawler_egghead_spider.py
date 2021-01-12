# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:56:09 2021

@author: hj99y
"""
import scrapy
#import sys
from importlib import reload
from scrapy.spiders import Spider
#from scrapy.selector import HtmlXPathSelector
from crawler_egghead.items import CrawlerEggheadItem
from datetime import datetime

from scrapy.http import Request
from scrapy.selector import Selector

#reload(sys)
#sys.setdefaultencoding('utf-8')

f1 = open("C:\\Users\\hj99y\\Desktop\\github\\crawling\\result\\egghead.txt", 'r')
egghead_links = []
while True:
    line = f1.readline()
    if not line : break
    line = line[:-1]
    egghead_links.append(line)
#print(egghead_links)
f1.close()
f1 = open("C:\\Users\\hj99y\\Desktop\\github\\crawling\\result\\egghead_img.txt", 'r')
eggheadImgs = []
while True:
    line = f1.readline()
    if not line : break
    line = line[:-1]
    eggheadImgs.append(line)
f1.close()
#print(eggheadImgs)


class crawler_egghead_Spider(scrapy.Spider):
    name = "egghead"  #spider 이름
    allowed_domains = ["egghead.io"]  #최상위 도메인
    #start_urls = ["https://egghead.io/search"]

    def start_requests(self):
        #for i in range(0, len(egghead_links), 1):
        for i in range(0, 3, 1):
            yield scrapy.Request(egghead_links[i], self.parse_egghead)

    def parse_egghead(self, response):
        item = CrawlerEggheadItem()
        item['lectureName'] = response.xpath('//h1/text()').extract()[0]
        item['price'] = -1  # 사이트 자체가 년간 멤버십
        #item['thumbnail']
        item['level'] = 6 #unknown 나중에 코드 돌려보기
        item['lecturer'] = response.xpath('//h2/text()').extract()[0]  # ==extract_first()
        item['siteIdx'] = 8 #Egghead
        item['rating'] = float(response.xpath('//*[@id="App-react-component"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div[6]/strong/text()').extract()[0])
        item['contents'] = response.xpath('//*[@id="App-react-component"]/div/div[2]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/a/div/h2/text()').extract()
        #item['category'] = 'unknown'
        item['subCategory'] = response.xpath('//*[@id="App-react-component"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/a/span/text()').extract()
        item['type'] = "on" #online
        item['language'] = "en" #English

        #시간을 분 단위로
        initialDuration = response.xpath('//*[@id="App-react-component"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/span/text()').extract()[0]
        if (initialDuration.find('h') != -1):
            hour = int(initialDuration.split('h')[0])
            minute = int(initialDuration.split('h')[1].split()[0].split('m')[0])
            item['totalDuration'] = hour * 60 + minute
        else:
            minute = int(initialDuration.split('m')[0])
            item['totalDuration'] = minute
        item['numOfLectures'] = len(item['contents'])
        print(item)
    """
    #text 내용은 url 뒤에 /text()
    #tag는 url 뒤에 /@ 하고 tag이름 ex. /@href
    #data만 출력은 xpath().extract()
    #tag 조건 제약 ex. href가 "image"를 포함하는 a가져오기 -> //a[contains(@href, "image")]/@href
 ################ 
    #1번만 실행
    def start_requests(self):
        for i in range(1,5,1):
            yield scrapy.Request("http://www.jobkorea.co.kr/starter/?schPart=10016&Page={0}".format(i),self.parse)
 
    #아이템 parse
    def parse(self, response):
        for colum in  response.xpath('//div[@class="filterListArea"]/ul/li') :
            item = CrawlerEggheadItem() 
            item['company'] = colum.xpath('div/div[@class="coTit"]/a/text()').extract_first() #주택명 추출
            item['context'] =colum.xpath('div/div[@class="tit"]//a/span/text()').extract_first()
            yield item
            
     """