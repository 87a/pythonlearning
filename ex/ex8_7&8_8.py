#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex8_7&8_8  文件名称
# DateTime:2021/7/16 21:36  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def make_album(singer, album, song=None):
    music = {'singer': singer, 'album': album}
    if song:
        music['song'] = song

    return music


# print(make_album('Alice', 'Algorithm'))
# print(make_album('Bob', 'Bank'))
# print(make_album('Carol', 'Cat', 10))
while True:
    singer = input("What's the name of the singer?(press q whenever you want to quit)")
    if singer != 'q':
        album = input("What's the name of the album?(press q whenever you want to quit)")
        if album != 'q':
            print(make_album(singer, album))
        else:
            break
    else:
        break
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
