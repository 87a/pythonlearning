#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:greeter  文件名称
# DateTime:2021/7/16 13:13  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
prompt = "If you tell us who you are,we can personalize the messages you see"
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello,{name}!")

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
