#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex9_13_dice  文件名称
# DateTime:2021/7/17 20:59  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
from random import randint


# import time
# start = time.perf_counter()
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


dice1 = Die()
for i in range(0, 10):
    dice1.roll_die()

dice2 = Die(10)
for i in range(0, 10):
    dice2.roll_die()
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
