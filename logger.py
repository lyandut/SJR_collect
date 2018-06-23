#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
from static_info import LOG_FILE_INFO

class Logger:
    def __init__(self, path, clevel=logging.DEBUG, flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        ch.setLevel(clevel)
        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(flevel)
        # handler添加到logger
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)

logger_info = Logger(LOG_FILE_INFO, logging.ERROR, logging.DEBUG)

# if __name__ == '__main__':
#     logger_info.debug('一个debug信息')
#     logger_info.info('一个info信息')
#     logger_info.war('一个warning信息')
#     logger_info.error('一个error信息')
#     logger_info.cri('一个致命critical信息')