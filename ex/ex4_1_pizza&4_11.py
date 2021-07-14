#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex4_1_pizza  文件名称
# DateTime:2021/7/13 17:50  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
pizzas = ['beef pizza', 'pepperoni pizza', 'pork pizza']
for pizza in pizzas:
    print(f"I like {pizza}.")
print("I really love pizza")

friend_pizzas = pizzas[:]
pizzas.append('mutton pizza')
friend_pizzas.append('carrot pizza')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
