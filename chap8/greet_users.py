#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:greet_users  文件名称
# DateTime:2021/7/17 15:26  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
