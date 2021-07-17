#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex8_9&8_10&8_11  文件名称
# DateTime:2021/7/17 16:09  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        sent_messages.append(message)
        print(message)


messages = ["I love you.", "How are you?", "What do you do?"]
sent_messages = []
# show_messages(messages)
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
