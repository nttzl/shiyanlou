#-*- coding:utf-8 -*-
import scrapy
from shiyanlou.items import RepsItem

class SYLGitSpider(scrapy.Spider):
    name = 'reps'

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for rep in response.css('li.public'):
            yield RepsItem({
                'name':rep.xpath('.//h3/a/text()').extract_first().strip(),
                'update_time':rep.xpath('.//relative-time/@datetime').extract_first()
                })

