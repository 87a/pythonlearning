#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex10_1_python_learning  文件名称
# DateTime:2021/7/18 11:02  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# import time
# start = time.perf_counter()
file_name = 'learning_python.txt'

with open(file_name) as file_object:
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'C').rstrip())




# print(contents)
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
