# !usr/bin/env python
# _*_ coding:utf-8 _*_
import threading
from Queue import Queue
from SJR_spider import SJR_Spider
from static_info import MAX_THREAD_COUNT, JOURNAL_COLLECTION, MATCH_COLLECTION, START_CODE, END_CODE
from proj.tasks import op_on_mongo_match_collection
from SJR_mongodb import SJR_mongodb
import traceback

def get_journal_info(cate_list):
    queue = Queue()
    threads = []
    lock = threading.Lock()
    cate_info = {}
    for i in xrange(MAX_THREAD_COUNT):
        t = SJR_Spider(lock=lock, queue=queue, result=cate_info)
        threads.append(t)
    for cate_code in cate_list:
        queue.put(cate_code)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # 考虑一个journal分属多个categories
    journal_info = {}
    for cate, jour_list in cate_info.items():
        for each in jour_list:
            journal_info.setdefault(each, [])
            journal_info[each].append(cate)

    return journal_info

def main():
    cate_list = range(START_CODE, END_CODE)
    journal_info = get_journal_info(cate_list)
    print len(journal_info)

    mongo_obj = SJR_mongodb()
    mongo_obj.insert_journal_collection(journal_dict=journal_info)
    print '{} update success!'.format(JOURNAL_COLLECTION)
    mongo_obj.close()

    for journal in journal_info:
        op_on_mongo_match_collection.apply_async(args=(journal, journal_info))

'''
领域划分需求，利用celery并发写入MongoDB
'''
if __name__ == '__main__':

    main()

'''
领域划分需求，单进程写入MongoDB
'''
# if __name__ == '__main__':
#
#     cate_list = range(START_CODE, END_CODE)
#     journal_info = get_journal_info(cate_list)
#     print len(journal_info)
#
#     mongo_obj = SJR_mongodb()
#
#     try:
#         mongo_obj.insert_journal_collection(journal_dict=journal_info)
#         print '{} update success!'.format(JOURNAL_COLLECTION)
#
#         mongo_obj.match_journal_area_categories(journal_dict=journal_info)
#         print '{} update success!'.format(MATCH_COLLECTION)
#     except Exception, e:
#         print e.message
#         print traceback.format_exc()
#
#     mongo_obj.close()