# !usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import re
from static_info import BASE_URL
from lxml import etree

class SJR_Spider(object):

    def __init__(self, result, pagenum, cate_code):
        self.result = result
        self.page_num = pagenum
        self.cate_code = cate_code

    def get_info(self):

        result_dict = {}
        try:
            # https://www.scimagojr.com/journalrank.php?category=2502&area=2500&page=2&total_size=91
            params = {'area': 2500, 'category': self.cate_code, 'page': self.page_num}
            resp = requests.get(BASE_URL, params=params)
            outp = resp.text
            # print resp.text

            # 处理文本
            # xpath抓取信息
            selector = etree.HTML(outp)
            # /html/body/div[6]/div[7]/table/tbody/tr[1]/td[2]/a
            journal = selector.xpath('/html/body/div[@class="ranking_body"]/div[@class="table_wrap"]/table/tbody/tr/td[@class="tit"]/a/text()')
            print journal

        except Exception, e:
            print e.message

    def get_total_size(self):
        try:
            params = {'area': 2500, 'category': self.cate_code}
            resp = requests.get(BASE_URL, params)
            outp = resp.text
            selecor = etree.HTML(outp)
            pagination = selecor.xpath('//div[@class="pagination"]/text()')[0]
            total_size = re.search(r'\d+$', pagination).group()
            print int(total_size)
        except Exception, e:
            print e.message

if __name__ == '__main__':
    result = {}
    pagenum = 1
    catecode = 2502
    obj = SJR_Spider(result, pagenum, catecode)
    obj.get_total_size()