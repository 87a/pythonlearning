#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex5_8_admin_greeting  文件名称
# DateTime:2021/7/14 16:52  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
users = ['admin', 'Alice', 'Bob', 'Carol', 'Dave']
users.clear()
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print(f"Hello {user},thank you for logging in again.")
else:
    print("We need to find some users")
