#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex7_4_pizza_topping  文件名称
# DateTime:2021/7/16 14:20  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
while True:
    topping = input("What topping do you want?")
    if topping == 'quit':
        break
    else:
        print(f"We'll add {topping}")

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
