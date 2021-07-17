#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex8_14_car_info  文件名称
# DateTime:2021/7/17 16:42  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def make_car(brand, type, **info):
    info['brand'] = brand
    info['type'] = type
    return info


car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
