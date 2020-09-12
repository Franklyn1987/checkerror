#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 10:26:27
# @Author  : 崔立波 (baiyuexingchen@gmail.com)
# @Link    : https://github.com/Franklyn1987
# @Version : $Id$

#########################################
from setuptools import setup
import subprocess
com_list_o = 'pip list -o' 
# 执行命令并返回结果
p = subprocess.Popen(com_list_o, shell=True, stdout=subprocess.PIPE)
# 取命令返回结果，结果是一个二进制字符串，包含了我们上面执行pip list -o后展现的所有内容
out = p.communicate()[0]
# 二进制转utf-8字符串
out = str(out, 'utf-8')
subprocess.call("pip install requests")
subprocess.call("pip install python-docx")
setup(
    name='checkerror',
    version='1.0',
    description='百度检查错别字，修改标点符号格式',
    author='崔立波',
    author_email='cuilibo@gmail.com',
    url='https://github.com/Franklyn1987',
    py_modules=['correct_text','checkerror'],
)
