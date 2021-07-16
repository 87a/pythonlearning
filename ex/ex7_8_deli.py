#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex7_8_deli  文件名称
# DateTime:2021/7/16 15:15  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
sandwich_orders = ['fish sandwich', 'pastrami sandwich', 'chicken sandwich', 'pastrami sandwich', 'beef sandwich',
                   'pastrami sandwich']
finished_sandwiches = []
print("The pastrami sandwich has sold out.")
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    if made_sandwich != 'pastrami sandwich':
        finished_sandwiches.append(made_sandwich)
        print(f"I made your {made_sandwich}.")
    else:
        continue

print("---Sandwich made---")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
