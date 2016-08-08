#coding:utf-8

from django.shortcuts import render, render_to_response, redirect
from scholar.func import *


def show(request):
    return render_to_response('scholar/show_data.html')


@json_response
def get_spider_data(request):
    ret = {'data':None,'status':0,'message':None}
    if request.method!='GET':
        ret['message'] = 'use GET method'
        return ret
    ret['data'] = read_spider_log()
    ret['status'] = 1
    return ret
