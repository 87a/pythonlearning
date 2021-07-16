#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex6_9  文件名称
# DateTime:2021/7/14 21:21  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
favorite_places = {
    'Alice': ['Beijing', 'Shanghai'],
    'Bob': ['Wenzhou'],
    'Carol': ['Hangzhou', 'Chengdu', 'Harbin']
}
for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name}'s favorite place is")
        print(places[0])
    else:
        print(f"\n{name}'s favorite places are")
        for place in places:
            print(place)
