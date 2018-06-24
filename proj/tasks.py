#!usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from proj.celery import app
from logger import logger_info
from SJR_mongodb import SJR_mongodb
from static_info import MATCH_COLLECTION, SUBJECT_AREA

@app.task
def op_on_mongo_match_collection(journal, journal_dict):
    mongo_obj = SJR_mongodb()
    match_collection = mongo_obj.database[MATCH_COLLECTION]
    insert_item = {}

    for i in range(9):
        collection = mongo_obj.database["mag_papers_" + str(i)]
        cursor = collection.find({'venue': journal}, {'title': 1, 'id': 1}, no_cursor_timeout=True)  # 设置cursor永不超时
        try:
            for doc in cursor:
                print '{} match with {}'.format(doc['_id'], journal)
                insert_item['_id'] = doc['_id']
                insert_item['title'] = doc['title']
                insert_item['id'] = doc['id']
                insert_item['venue'] = journal
                insert_item['subject_area'] = SUBJECT_AREA
                insert_item['subject_categories'] = journal_dict[journal]
                match_id = match_collection.save(insert_item)
                insert_item.clear()
                logger_info.info('{} insert success!'.format(match_id))
        finally:
            cursor.close()
    logger_info.info('{} match success!'.format(journal))
    mongo_obj.close()