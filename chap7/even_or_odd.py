#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:even_or_odd.py  文件名称
# DateTime:2021/7/16 13:36  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
