#!usr/bin/env python
# -*- coding:utf-8 -*-

# broker_url = 'redis://127.0.0.1:6379'
# broker_transport = 'redis'
#
# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# timezone = 'Asia/Shanghai'
# enable_utc = True
#
# # unregistered task of type
# imports = ("proj.tasks",)


# 启动命令(并发50个worker): celery -A proj worker -c 50 -l info
# 尽量寻求合适的配置参数，celery经常出现假死情况
BROKER_URL = 'redis://127.0.0.1:6379/0'
BROKER_TRANSPORT = 'redis'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_IMPORTS = ("proj.tasks",)
CELERYD_FORCE_EXECV = True        # 防止死锁
# CELERYD_TASK_TIME_LIMIT = 60    # 单个worker超时时间，时间太长，不应该设置该值