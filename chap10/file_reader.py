#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:file_reader  文件名称
# DateTime:2021/7/17 21:31  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# import time
# start = time.perf_counter()
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
