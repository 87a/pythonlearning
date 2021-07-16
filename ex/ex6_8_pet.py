#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex6_8_pet  文件名称
# DateTime:2021/7/14 21:16  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
pet1 = {
    'kind': 'dog',
    'owner': 'Alice',
}
pet2 = {
    'kind': 'cat',
    'owner': 'Bob',
}
pets = [pet1, pet2]
for pet in pets:
    print(pet)
