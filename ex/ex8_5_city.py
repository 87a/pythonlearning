#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex8_5_city  文件名称
# DateTime:2021/7/16 20:53  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def describe_city(city, country='China'):
    print(f"{city.title()} is in {country.title()}")


describe_city('wenzhou')
describe_city('hangzhou')
describe_city('brooklyn', 'america')
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
