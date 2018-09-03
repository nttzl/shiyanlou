# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from douban_movie.items import MovieItem


class AwesomeMovieSpider(scrapy.spiders.CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/subject/3011091']

    rules = (
        Rule(LinkExtractor(allow=r'https://movie.douban.com/subject/.+/?from=subject-page'),callback="parse_movie_item",follow=True),
    )
    def parse_movie_item(self, response):
        item = MovieItem()
        item['url'] = response.url
        item['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first()
        item['summary'] = response.xpath('//span[@property="v:summary"]/text()').extract_first().strip()
        item['score'] = float(response.css('strong.rating_num::text').extract_first().strip())
        if item['score'] >= 8:
            yield item

