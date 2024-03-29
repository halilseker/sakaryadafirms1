# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


# import sqlite3


class MongodbPipeline(object):
    collection_name = "sakaryafirms1"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
            "mongodb+srv://hiseker:adiyla83bit@cluster0-fj10c.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client["TEKNOKENT"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
