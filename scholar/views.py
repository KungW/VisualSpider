#coding:utf-8

from django.shortcuts import render, render_to_response, redirect
from scholar.func import *
from .SearchPageInfoGenerator import StoreInfoGenerator


def show(request):
    return render_to_response('scholar/show_data.html')

@json_response
def get_store_info(request):
    ret = {'data': None, 'status': 0, 'message': None}
    if request.method != 'GET':
        ret['message'] = 'use GET method'
        return ret
    store_url = request.GET.get('store_url')
    print('url:',store_url)
    res = StoreInfoGenerator(store_url).to_json()
    print(res)
    if res not in [-1,-2]:
        ret['status'] = 1
        ret['data'] = res
    else:
        print('ret={}'.format(res))
        ret['status'] = res
        if res==-1:
            ret['message'] = 'Locate error'
        else:
            ret['message'] = 'Merge Error'
    return ret

'''
@json_response
def get_spider_data(request):
    ret = {'data':None,'status':0,'message':None}
    if request.method!='GET':
        ret['message'] = 'use GET method'
        return ret
    ret['data'] = read_spider_log()
    ret['status'] = 1
    return ret
'''