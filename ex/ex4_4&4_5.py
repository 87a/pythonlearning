#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex4_4_million  文件名称
# DateTime:2021/7/13 19:49  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
import time

nums = []
for i in range(1, 1000001):
    nums.append(i)
# for num in nums:
#     print(num)
print(max(nums))
print(min(nums))
start = time.perf_counter()
print(sum(nums))
end = time.perf_counter()
print(end - start)
