# -*- coding: utf-8 -*-
#Scrapes from a specific subreddit - /r/politics
#Scrapes title of a thread and corresponding comments

#Scrapy spider borrowed & modified: 
#https://github.com/asabine/reddit_crawler/blob/master/reddit_crawler/spiders/reddit.py


from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
import scrapy

class SomeItems(Item):
    title = Field()
    comments = Field()

class RedditbotSpider(CrawlSpider):
    name = 'RedditbotSpider'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/news/top/']
    custom_settings = {
            'BOT_NAME': 'RedditbotSpider',
            'DEPTH_LIMIT': 5,
            'DOWNLOAD_DELAY': 3
            }
    rules = [
        Rule(LinkExtractor(allow=['/r/news/top/\?count=\d*&after=\w*']),
             callback='parse_item',
             follow=True)
    ]
    
    def parse(self, response):
        selector_list = response.css('div.thing')
        
        for selector in selector_list:
            item = SomeItems()
            item['title'] = selector.xpath('div[2]/div/p[1]/a/text()').extract()
            
            follow = selector.xpath('div[2]/div/ul/li[1]/a/@href').extract()[0]   
            request = scrapy.Request(follow , 
                                     callback=self.tofollow)
									 
            request.meta['item'] = item
            yield request
                      
    def tofollow(self,response):
        item = response.meta['item']
        comment_list = response.css('div.entry')
        for comment in comment_list[1:]:
            item['comments'] = comment.xpath('form/div/div/p/text()').extract()
            yield item
