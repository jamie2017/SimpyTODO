#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jianmei Ye
@file: urls.py.py
@time: 1/4/18 5:45 PM
"""


from django.conf.urls import url
from todo.views import index, delete, add, complete, filter_index

urlpatterns = [
    url(r'^delete/(?P<pk>\d+)/$', delete),
    url(r'^complete/(?P<pk>\d+)/$', complete),
    url(r'^add/', add),
    url(r'^(?P<pk>\w+)/$', filter_index),
    url(r'^$', index),
]