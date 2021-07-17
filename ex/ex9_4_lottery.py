#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex9_4_lottery  文件名称
# DateTime:2021/7/17 21:02  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
from random import randint

# import time
# start = time.perf_counter()
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
results = []
for i in range(0, 4):
    results.append(choices[randint(0, 14)])

for result in results:
    print(result, end=" ")


def judge_same(list1, list2):
    count = 0
    for a in list1:
        if a in list2:
            count += 1
        else:
            return False

    for a in list2:
        if a in list1:
            count += 1
        else:
            return False
    return True


# print(judge_same(['a', 'b', 'c', 'd'], ['d', 'c', 'b', 'a']))
count = 0
guesses = []
while True:
    guesses.clear()
    for i in range(0, 4):
        guesses.append(choices[randint(0, 14)])
    count += 1
    if judge_same(guesses,results):
        print(guesses)
        print(count)
        break

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
