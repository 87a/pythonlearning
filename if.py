#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:if  文件名称
# DateTime:2021/7/14 15:35  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# 用==检查相等
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 检查相等时区分大小写
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

# 用!=检查不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 数值比较
print(18 > 47)
print(18 < 47)
print(18 == 47)
print(18 != 47)

# 检查多个条件
age = 20
if age >= 18 and age <= 22:
    print('valid age')
if age > 20 or age <= 20:
    print('valid age')

# 检查特定值是否在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('mushroom' not in requested_toppings)

# elif用法
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

# 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# 确定列表不是空的
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
