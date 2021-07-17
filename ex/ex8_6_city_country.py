#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex8_6_city_country  文件名称
# DateTime:2021/7/16 21:28  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'


print(city_country('santiago', 'Chile'))
print(city_country('wenzhou', 'China'))
print(city_country('hangzhou', 'china'))
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
