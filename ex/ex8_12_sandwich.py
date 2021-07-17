#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:sandwich  文件名称
# DateTime:2021/7/17 16:39  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def make_sandwich(*toppings):
    print("\nYou ordered a sandwich with:")
    for topping in toppings:
        print(topping)


make_sandwich('cucumber')
make_sandwich('fish', 'beef')
make_sandwich('mutton', 'pork', 'apple')
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
