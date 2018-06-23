# !usr/bin/env python
# _*_ coding:utf-8 _*_
'''
Created on Jun 4, 2018

@author: Li_Yan
'''
from pymongo import MongoClient
from logger import logger_info
from static_info import JOURNAL_COLLECTION, SUBJECT_AREA, MATCH_COLLECTION

class SJR_mongodb(object):
    def __init__(self):

        self.clientRW = MongoClient('210.30.97.43',
                        username='userRW',
                        password='thealphaRW',
                        authSource='ms-datasets',
                        authMechanism='SCRAM-SHA-1')

        self.database = self.clientRW["ms-datasets"]

    def close(self):
        self.clientRW.close()

    def insert_journal_collection(self, journal_dict):
        my_collection = self.database[JOURNAL_COLLECTION]
        insert_item = {}
        for jour, cate_list in journal_dict.items():
            insert_item['journal'] = jour
            insert_item['subject_area'] = SUBJECT_AREA
            insert_item['subject_categories'] = cate_list
            insert_id = my_collection.save(insert_item)
            # 重点：清空字典
            # 报错：E11000 duplicate key error collection
            # 原因：共用一个外部变量，mongodb认为是同一条数据，太sb了
            insert_item.clear()
            logger_info.info('{} insert success!'.format(insert_id))

    def match_journal_area_categories(self, journal_dict):
        match_collection = self.database[MATCH_COLLECTION]
        insert_item = {}
        counter = 0
        for i in range(9):
            collection = self.database["mag_papers_" + str(i)]
            cursor = collection.find(no_cursor_timeout=True)  # 设置cursor永不超时
            try:
                for doc in cursor:
                    if "venue" in doc:
                        journal = doc["venue"]
                        if journal in journal_dict:
                            insert_item['_id'] = doc['_id']
                            insert_item['title'] = doc['title']
                            insert_item['id'] = doc['id']
                            insert_item['venue'] = journal
                            insert_item['subject_area'] = SUBJECT_AREA
                            insert_item['subject_categories'] = journal_dict[journal]
                            match_id = match_collection.save(insert_item)
                            logger_info.info('{} insert success!'.format(match_id))
                    else:
                        logger_info.error('{} has no venue!'.format(doc['_id']))
            finally:
                cursor.close()