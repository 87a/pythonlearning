#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:pets  文件名称
# DateTime:2021/7/16 15:50  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(pet_name='willie')
describe_pet('willie')
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
