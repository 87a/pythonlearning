#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:greet_user  文件名称
# DateTime:2021/7/16 15:28  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def greet_user(username):
    print(f"Hello,{username.title()}!")


greet_user('jesse')

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
