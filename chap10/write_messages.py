#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:write_messages  文件名称
# DateTime:2021/7/18 11:24  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# import time
# start = time.perf_counter()
filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming.")

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
