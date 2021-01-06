# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:56:09 2021

@author: hj99y
"""
import scrapy
import sys
from importlib import reload
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from crawler_egghead.items import CrawlerEggheadItem
from scrapy.http import Request
from scrapy.selector import Selector

reload(sys)
sys.setdefaultencoding('utf-8')
 

class crawler_egghead_Spider(scrapy.Spider):
    name = "crawler_egghead"  #spider 이름
    allowed_domains = ["https://egghead.io/"]  #최상위 도메인
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