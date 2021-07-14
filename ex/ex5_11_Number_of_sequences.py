#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex5_11_Number_of_sequences  文件名称
# DateTime:2021/7/14 17:22  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
nums = list(range(1,10))
for num in nums:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(f"{num}th")
