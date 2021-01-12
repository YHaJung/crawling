# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class CodeingCrawlerItem(scrapy.Item):
    lectureName = scrapy.Field()  # 강의명 string
    price = scrapy.Field()  # 가격 int
    lectureLink = scrapy.Field()  # 강의링크 string
    thumbnail = scrapy.Field()  # 썸네일 사진링크 string
    level = scrapy.Field()  # 강의레벨 int(1~5)/정보 없으면 추출/그래도 모르면 6
    lecturer = scrapy.Field()
    siteIdx = scrapy.Field()  # 사이트번호 int(기준??)
    rating = scrapy.Field()  # 평점(나중에 내부 리뷰평점으로 대체) - float1~5
    contents = scrapy.Field()  # 강의목차 - string
    category = scrapy.Field()
    subCategory = scrapy.Field()  # programming language
    type = scrapy.Field()  # 온라인/오프라인 string on/장소명
    language = scrapy.Field()  # 언어 한글이면 ko, 영어면 en
    totalDuration = scrapy.Field()  # 총 강의길이 int 분단위
    numOfLectures = scrapy.Field()  # 총 강의 개수 int
