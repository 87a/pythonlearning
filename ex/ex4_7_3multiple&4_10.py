#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex4_7_3multiple  文件名称
# DateTime:2021/7/13 20:33  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
multiples = []
for i in range(3,31,3):
    multiples.append(i)
for multiple in multiples:
    print(multiple)
print("The first three items in the list are:")
print(multiples[:3])
print("Three items from the middle of the list are:")
print(multiples[3:6])
print("The last three items in the list are:")
print(multiples[-3:])
