#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-28 08:29:30
# @Author  : 崔立波 (baiyuexingchen@gmail.com)
# @Link    : http://blog.sina.com.cn/dejavu1
# @Version : 1



import requests
import bs4

###############################################
#以下开始
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# import urllib
# import json
#client_id 为官网获取的AK， client_secret 为官网获取的SK
client_id =""#需要添加
client_secret =""#需要添加
def doc():
    print("txt_correction('需要检查的文字内容')")
#获取token
def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    token_content = response.read()
    if token_content:
        token_info = json.loads(token_content)
        token_key = token_info['access_token']
    return token_key

def txt_correction(content):
    token=get_token()
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/ecnet'
    params = dict()
    params['text'] = content
    params = json.dumps(params).encode('utf-8')
    access_token = token
    url = url + "?access_token=" + access_token
    request = urllib.request.Request(url=url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        content=content.decode('GB2312')
        data = json.loads(content)

        item=data['item']
        data1=json.loads(content)
    if item['score']>0:
        print ('【原文】：',data1['text'])
        print('【纠错后】：',item['correct_query'])
        print("【错误标注】：",item['vec_fragment'])
        print('【Score】：',item['score'])
        print("=============================")
    # else:
    #     print("✓")