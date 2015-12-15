# -*- coding=UTF-8 -*-
import scrapy
from myspider.items import MyspiderItem

class MeituanSpider(scrapy.Spider):

	name = "58cooker"
	# allowed_domains = ["dg.meituan.com"]  #美团网
	start_urls = ["http://huizhou.58.com/job/?key=%E5%8E%A8%E5%B8%88&cmcskey=%E5%8E%A8%E5%B8%88"]   #惠州厨师招聘信息

	def parse(self,response):
		
		for href in response.css('.infolist dl a::attr(href)'):

			full_url = response.urljoin(href.extract())
			yield scrapy.Request(full_url, callback=self.parse_cooker)

	def parse_cooker(self,response):
		items = MyspiderItem()
		yield {
		   'link':response.url,
		   'company':response.css('dd a::text').extract()[0],
		   'title':response.css('dl a::text').extract()[0],
		   'location':response.css('dd::text').extract()[0],
		   'gold':response.css('dd span a::text').extract()[0],
		   'online':response.css('dl span a::text').extract()[0],
		}

