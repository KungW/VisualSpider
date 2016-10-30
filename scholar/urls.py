#coding:utf-8
from django.conf.urls import url
from scholar.views import *

urlpatterns = [
    url(r'^show/$', show),
    #url(r'^get_spider_data/', get_spider_data),
]