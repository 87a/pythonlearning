#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:counting  文件名称
# DateTime:2021/7/16 13:59  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
import time
start = time.perf_counter()
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))
