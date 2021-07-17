#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:pizza.py  文件名称
# DateTime:2021/7/17 16:26  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
