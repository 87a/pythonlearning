#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:my_cars  文件名称
# DateTime:2021/7/17 20:47  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# from electric_car import Car, ElectricCar
import electric_car
# import time
# start = time.perf_counter()
my_beetle = electric_car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
