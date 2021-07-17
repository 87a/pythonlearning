#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:formatted_name  文件名称
# DateTime:2021/7/16 21:01  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)
print(get_formatted_name('jimi', 'hendrix'))
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
