# -*- coding:utf-8 -*-
import scrapy

class SYLGitSpider(scrapy.Spider):
    name = 'shiyanlou_github_respositories'
        
    @property
    def start_urls(self):

        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))
        
    def parse(self,response):
        for rep in response.xpath('//li[contains(@itemprop,"owns")]'):
            yield {
                'name':rep.xpath('.//h3/a/text()').extract_first().strip(),
                'update_time':rep.xpath('.//div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract_first()
            }


