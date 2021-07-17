#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:making_pizzas  文件名称
# DateTime:2021/7/17 16:45  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
# import pizza as p
# from pizza import make_pizza as mp
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
