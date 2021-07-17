#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:my_electric_car  文件名称
# DateTime:2021/7/17 20:44  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
from electric_car import ElectricCar

# import time
# start = time.perf_counter()
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
