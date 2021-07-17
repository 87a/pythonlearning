#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:ex9_3_user  文件名称
# DateTime:2021/7/17 17:24  当前时间
# SoftWare: PyCharm  创建文件的IDE名称
# import time
# start = time.perf_counter()
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name, self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print(f"Hello,{self.first_name} {self.last_name}")


class Privileges:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


admin1 = Admin('q', 'zz')
admin1.privileges.privileges = ["can add post", "can delete post", "can ban users"]
admin1.privileges.show_privileges()
# user1 = User('q', 'zz')
# user1.greet_user()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)
# end = time.perf_counter()
# print('Running time: %s Seconds' % (end - start))
