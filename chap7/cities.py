#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:cities  文件名称
# DateTime:2021/7/16 14:13  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you're finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
