#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:user_profile  文件名称
# DateTime:2021/7/17 16:33  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
