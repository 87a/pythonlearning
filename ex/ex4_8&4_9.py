#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex4_8_cube  文件名称
# DateTime:2021/7/13 20:36  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)
for cube in cubes:
    print(cube)
cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
    print(cube)
