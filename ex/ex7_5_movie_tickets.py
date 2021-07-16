#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex7_5_movie_tickets  文件名称
# DateTime:2021/7/16 14:23  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
while True:
    age = input("How old are you?")
    if age == 'quit':
        break
    elif int(age) <= 3:
        print("Your ticket is free!")
    elif 3 < int(age) <= 12:
        print("Your ticket price is $10")
    else:
        print("Your ticket price is $15")

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
