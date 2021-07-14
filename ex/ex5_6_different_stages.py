#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex_5_6_different_stages  文件名称
# DateTime:2021/7/14 16:16  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
age = int(input())
if age < 2:
    print("婴儿")
elif 2 <= age < 4:
    print("幼儿")
elif 4 <= age < 13:
    print("儿童")
elif 13 <= age < 20:
    print("青少年")
elif 20 <= age <= 65:
    print("成年人")
else:
    print("老年人")
