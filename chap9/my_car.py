#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:my_car  文件名称
# DateTime:2021/7/17 20:37  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
from car import Car

# import time
# start = time.perf_counter()
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
