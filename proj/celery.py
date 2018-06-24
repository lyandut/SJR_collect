#!usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from celery import Celery

app = Celery('proj',
             broker='redis://localhost:6379/0',
             # include=['proj.tasks']
             )

app.config_from_object('proj.config')

if __name__ == '__main__':
    app.start()





