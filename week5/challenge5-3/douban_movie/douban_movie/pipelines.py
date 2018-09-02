# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import json
import redis


class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        item['summary'] = re.sub('\s+', ' ', item['summary'])
#        self.redis.lpush('douban_movie:items',json.dumps(dict(item)))

        return item

#    def open_spider(self,spider):
#        self.redis = redis.StrictRedis()
