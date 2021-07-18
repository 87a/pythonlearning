#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:pi_string  文件名称
# DateTime:2021/7/18 10:51  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# import time
# start = time.perf_counter()
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday,in the form mmddyy")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi")
else:
    print("Your birthday does not appear in the first million digits of pi")
# print(f"{pi_string[:52]}...")
# print(len(pi_string))
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
