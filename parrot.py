#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:parrot  文件名称
# DateTime:2021/7/16 13:11  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
import time
start = time.perf_counter()
message = input("Tell me something,and I will repeat it back to you:\n")
print(message)
end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))
