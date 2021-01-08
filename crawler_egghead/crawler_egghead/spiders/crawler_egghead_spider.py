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
from crawler_egghead.crawler_egghead.items import CrawlerEggheadItem
from datetime import datetime
import selenium.webdriver as webdriver

from scrapy.http import Request
from scrapy.selector import Selector

#reload(sys)
#sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome('C:\\Users\\hj99y\\downedprograms\\chromedriver')


class crawler_egghead_Spider(scrapy.Spider):
    name = "egghead"  #spider 이름
    allowed_domains = ["egghead.io"]  #최상위 도메인
    #start_urls = ["https://egghead.io/search"]
    def start_requests(self):
        for i in range(1, 2, 1):
            yield scrapy.Request("https://egghead.io/search&page=%d" % i, self.parse_egghead)

    def parse_egghead(self, response):
        for sel in response.xpath(''):
            item = CrawlerEggheadItem()
            item['lecturer'] = sel.xpath('').extract()[0]  #==extract_first()
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
            #//*[@id="devStarterForm"]/div[2]/ul/li[1]/div[1]/div[1]/a