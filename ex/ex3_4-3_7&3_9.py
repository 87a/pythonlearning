#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex3_4-3_7  文件名称
# DateTime:2021/7/12 21:25  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
guests = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']
for guest in guests:
    print(f"I want to invite {guest} to my dinner")

print(f"{guests[2]} can't go to my dinner")
guests[2] = 'Frank'
for guest in guests:
    print(f"I want to invite {guest} to my dinner")

print("I found a bigger table")
guests.insert(0, "Ghost")
guests.insert(4, 'Jack')
guests.append('Kevin')

for guest in guests:
    print(f"I want to invite {guest} to my dinner")

print("Sorry,I can only invite two guests")

while (len(guests) > 2):
    popped_guest = guests.pop()
    print(f"{popped_guest},I'm sorry that I can't invite you to dinner")

for guest in guests:
    print(f"I want to invite {guest} to my dinner")
print(f"I invited {len(guests)} guests to dinner")
del guests[1], guests[0]
print(guests)
