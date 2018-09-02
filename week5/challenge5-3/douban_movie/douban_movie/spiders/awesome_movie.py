# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from douban_movie.items import MovieItem


count = 0
class AwesomeMovieSpider(scrapy.spiders.CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/subject/3011091']

    rules = (
        Rule(LinkExtractor(allow='https://movie.douban.com/subject/\d+/\?from=subject-page'),callback="parse_start_url",follow=True)
    )
    def parse_movie_item(self, response):
        global count
        item = MovieItem()
        item['url'] = response.url
        item['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()
        item['summary'] = response.xpath('//span[@class="all hidden"]/text()').extract()
        item['score'] = float(response.css('strong.rating_num::text()').extract().strip())
        if item['score'] >= 8:
            yield item
            count += 1
        if count <= 35:
            yield self.parse_page(response)

    def parse_start_url(self, response):
        yield self.parse_movie_item(response)

    def parse_page(self, response):
        yield self.parse_movie_item(response)
