# !usr/bin/env python
# _*_ coding:utf-8 _*_
import threading
from Queue import Queue
from SJR_spider import SJR_Spider
from static_info import MAX_THREAD_COUNT, CATEGORY_CODE


def get_journal_info(cate_list):
    queue = Queue()
    threads = []
    lock = threading.Lock()
    journal_info = {}
    for i in xrange(MAX_THREAD_COUNT):
        t = SJR_Spider(lock=lock, queue=queue, result=journal_info)
        threads.append(t)
    for cate_code in cate_list:
        queue.put(cate_code)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print 'JOURNAL INFO Done!'
    return journal_info

if __name__ == '__main__':
    cate_list = range(2501, 2510)
    journal_info = get_journal_info(cate_list)
    for each in journal_info.items():
        print each