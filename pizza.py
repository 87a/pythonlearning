#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:pizza  文件名称
# DateTime:2021/7/14 20:31  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t"+topping)
