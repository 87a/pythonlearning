#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:tuple  文件名称
# DateTime:2021/7/13 21:05  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# 创建和访问元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 遍历
for dimension in dimensions:
    print(dimension)

# 修改整个元组
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
