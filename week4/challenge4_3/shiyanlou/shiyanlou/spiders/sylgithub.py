# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import RepsItem


class SylgithubSpider(scrapy.Spider):
    name = 'reps'
    
    @property
    def start_urls(self):
        return ('http://www.github.com/shiyanlou?page={}&tab=repositories'.format(i) for i in range(1,5))

    def parse(self, response):
        for rep in response.css('li.public'):
            item = RepsItem()
            item['name'] = rep.xpath('.//a/text()').extract_first().strip()
            item['update_time'] = rep.xpath('.//relative-time/@datetime').extract_first()
            url = response.urljoin(rep.xpath('.//a/@href').extract_first())
            request = scrapy.Request(url,callback=self.parse_reps)
            request.meta['item'] = item
            yield request

    def parse_reps(self, response):
        item = response.meta['item']
        item['commits'] = response.css('span.num::text').extract()[0].strip()
        item['branches'] = response.css('span.num::text').extract()[1].strip()
        item['releases'] = response.css('span.num::text').extract()[2].strip()
        yield item


