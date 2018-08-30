# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from shiyanlou.models import engine,Repository
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(item['update_time'],'%Y-%m-%dT%H:%M:%SZ') 
        x = item['commits']
        x = x.replace(',','')
        item['commits'] = int(x)
        item['branches'] = int(item['branches'])
        y = item['releases']
        y = y.replace(',','')
        item['releases'] = int(y)

        self.session.add(Repository(**item))
        return item

    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
