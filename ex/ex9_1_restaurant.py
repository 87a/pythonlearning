#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex9_1_restaurant  文件名称
# DateTime:2021/7/17 17:12  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name},its cuisine type"
              f" is {self.cuisine_type}.")

    def set_number_served(self, number):
        self.number_served = number
        print(f"number_served = {self.number_served}")

    def increment_number_served(self, inc_number):
        self.number_served += inc_number

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is opening now!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavors(self, flavor):
        self.flavors.append(flavor)

    def describe_icecreamstand(self):
        print(f"name:{self.restaurant_name} cuisine type:{self.cuisine_type}")
        print("flavors:")
        for flavor in self.flavors:
            print(flavor)


# my_res = Restaurant('Gold chops', 'chinese meal')
# my_res.describe_restaurant()
# my_res.open_restaurant()
my_ice = IceCreamStand("love", "Chinese ice cream")
my_ice.flavors.append("apple")
my_ice.describe_icecreamstand()
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
