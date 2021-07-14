#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:jiugongge  文件名称
# DateTime:2021/7/13 16:12  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
import itertools

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
results = list(itertools.permutations(nums))
count = 0
for result in results:
    if (result[0] + result[3] + result[6] == 15 and result[1] + result[4] + result[7] == 15
            and result[0] + result[1] + result[2] == 15 and result[3] + result[4] + result[5] == 15
            and result[0] + result[4] + result[8] == 15 and result[2] + result[4] + result[6] == 15):
        count = count + 1
        print(count, end="")
        print(".\n", end="")
        for i in range(0, 9):
            print(result[i], end="")
            if (i + 1) % 3 == 0:
                print()
            else:
                print(" ", end="")
