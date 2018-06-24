#!usr/bin/env python
# -*- coding:utf-8 -*-

broker_url = 'redis://127.0.0.1:6379'
broker_transport = 'redis'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True

# unregistered task of type
imports = ("proj.tasks",)


