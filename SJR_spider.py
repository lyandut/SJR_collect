# !/usr/bin/env python
# _*_ coding:utf8 _*_
import requests
import threading
import Queue
from lxml import etree
import re
from static_info import BASE_URL, CATEGORY_CODE

class SJR_Spider(threading.Thread):

    def __init__(self, queue, lock, result):
        threading.Thread.__init__(self)
        self.data = queue
        self.lock = lock
        self.result = result

    def get_total_size(self):
        try:
            params = {'area': 2500, 'category': self.cate_code}
            resp = requests.get(BASE_URL, params)
            outp = resp.text
            selecor = etree.HTML(outp)
            pagination = selecor.xpath('//div[@class="pagination"]/text()')[0]
            total_size = re.search(r'\d+$', pagination).group()
            return int(total_size)
        except Exception, e:
            print e.message

    def get_info(self):
        result_list = []
        total_size = self.get_total_size()
        if total_size % 50 == 0:
            page_size = total_size / 50
        else:
            page_size = total_size / 50 + 1

        for page in range(1, page_size+1):
            try:
                params = {'area': 2500, 'category': self.cate_code, 'page': page}
                resp = requests.get(BASE_URL, params=params)
                outp = resp.text
                # print resp.text
                # 处理文本
                # xpath抓取信息
                selector = etree.HTML(outp)
                # /html/body/div[6]/div[7]/table/tbody/tr[1]/td[2]/a
                journal_list = selector.xpath('/html/body/div[@class="ranking_body"]/div[@class="table_wrap"]/table/tbody/tr/td[@class="tit"]/a/text()')
                print 'cate-{} page-{} is ok!'.format(self.cate_code, page)
                result_list.extend(journal_list)
            except Exception, e:
                print e.message
        return result_list

    def run(self):
        while True:
            try:
                self.cate_code = self.data.get(1, 5)
                result_list = self.get_info()
                if self.lock.acquire():
                    self.result[CATEGORY_CODE[self.cate_code]] = result_list
                    self.lock.release()
                print 'cate-{} is ok!'.format(self.cate_code)
            except Queue.Empty:
                break
            except Exception, e:
                print 'Cannot get info from cate_code ({})! Reason: {}'.format(self.cate_code, e)
                self.lock.release()
                break

if __name__ == '__main__':
    pass

