#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:hello_world  文件名称
# DateTime:2021/7/12 15:39  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
import time

start = time.perf_counter()

message = "Hello Python world!"
print(message)
# python始终记录变量的最新值
message = "Hello Python Crash Course world!"
print(message)

# 字符串可用单引号,也可用双引号
'This is a string'
"This is also a string"

# title()会使每个单词首字母大写
name = "ada lovelace"
print(name.title())

# upper()和lower()使所有字母变为大写或小写
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# f字符串
first_name = "ada"
last_name = "lovalace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello,{full_name.title()}!")
message = f"Hello,{full_name.title()}!"
print(message)

# 制表符和换行符
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 删除空白
favorite_language = " python "
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())
end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))
