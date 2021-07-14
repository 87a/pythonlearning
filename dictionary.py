#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:dictionary  文件名称
# DateTime:2021/7/14 17:26  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# 字典的创建与访问
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0['color'])

# 删除键值对
del alien_0['points']
print(alien_0)

# 多行字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(language)

# 使用get()访问值(如果指定的值可能不存在)
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned')
speed_value = alien_0.get('speed', 'No point value assigned')
print(point_value)
print(speed_value)

# 遍历字典
for key, value in alien_0.items():
    print(f"\nkey:{key}")
    print(f"value:{value}")

# 遍历键
for key in alien_0.keys():
    print(key)

# 按特定顺序遍历键
for name in sorted(favorite_languages.keys()):
    print(name)

# 遍历值
for value in favorite_languages.values():
    print(value)

for value in set(favorite_languages.values()):  # 剔除重复项
    print(value)
