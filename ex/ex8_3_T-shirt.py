#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex8_3_T-shirt  文件名称
# DateTime:2021/7/16 20:48  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def make_shirt(size='L', sentence="I love python"):
    print(f'The size of the T-shirt is {size},it\'s sentence is "{sentence}"')


# make_shirt('L', 'love')
# make_shirt(sentence='peace', size='M')
make_shirt()
make_shirt(size='M')
make_shirt('L', 'love')
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
