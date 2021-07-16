#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:list  文件名称
# DateTime:2021/7/12 17:05  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

import time

start = time.perf_counter()
# 创建列表
bicycles = ['trek', 'cannonale', 'redline', 'specialized']
print(bicycles)

# 访问元素
print(bicycles[0])
# -1可访问最后一个元素,其他负数同理
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 通过下标修改元素的值
# motorcycles[0] = 'ducati'
# print(motorcycles)

# 通过append()在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

# 使用insert()在列表中添加元素
motorcycles.insert(0, 'yadea')
print(motorcycles)

# 使用del()删除指定位置元素
del motorcycles[0]
print(motorcycles)

# 使用pop()删除列表末尾的元素
popped_motorcycle = motorcycles.pop(2);
print(motorcycles)
print(popped_motorcycle)

# 使用remove()根据值删除元素
motorcycles.remove('yamaha')
print(motorcycles)

# 使用sort()对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# 加入reverse=True可反向排序
cars.sort(reverse=True)
print(cars)

# 使用sorted()对列表临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)

# 使用reverse()倒转列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 使用len()获取列表长度
print(len(cars))
end = time.perf_counter()

# 使用for遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}\n")
print("Thank you,everyone.That was a great magic show")
print('Running time: %s Seconds' % (end - start))

# 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# 简单统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[0:3:2])
print(players[2:])
print(players[-3:])

# 遍历切片
for player in players[:3]:
    print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
