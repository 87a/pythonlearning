#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex7_2_restaurant_book  文件名称
# DateTime:2021/7/16 13:52  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
num_of_people = int(input("How many people are going to have meals?"))
if num_of_people > 8:
    print("Sorry, There is no table for you.")
else:
    print("There is a table for you")
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
