#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:favorite_languages  文件名称
# DateTime:2021/7/14 20:35  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
        print("\t"+languages[0].title())
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
