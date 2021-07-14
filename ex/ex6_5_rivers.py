#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex6_5_rivers  文件名称
# DateTime:2021/7/14 19:46  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
rivers = {'nile': 'egypt', 'changjiang': 'china', 'mississippi': 'america'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

