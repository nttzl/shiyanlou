# -*- coding:utf-8 -*-
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    name = 'shiyanlou-courses'
    @property    
    def start_urls(self):
        url_tmpl = 'http://www.shiyanlou.com/courses/{}'
        return (url_tmpl.format(i) for i in range(1,23))

    def parse(self,response):
        for course in response.xpath('//div[@class="content course-infobox"]'):
            yield {
                'name': course.css('div h4 span::text').extract_first(),
                'description': course.css('p::text').extract_first(),
                'type': course.css('span.course-infobox-type::text').extract_first(),
                'students': course.xpath(".//div[@class='course-info-details']/span/text()").extract_first()
            }
