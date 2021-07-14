#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex5_10_check_username  文件名称
# DateTime:2021/7/14 17:12  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
current_users = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']
current_users2 = [value.lower() for value in current_users]
new_users = ['Amy', 'bob', 'carol', 'David', 'john']
for new_user in new_users:
    if new_user.lower() in current_users2:
        print("It's used by someone,try another name.")
    else:
        print("It's not used.")
