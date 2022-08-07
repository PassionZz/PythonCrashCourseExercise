"""
@creat_time 2022/8/7 15:17
@creat_by PassionZz
@file_name 9-7
@description 管理员
"""
import importlib


class User():
    

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        print("Hello," + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """管理员类，用户类的子类"""

    def __init__(self, first_name, last_name, privileges=[
        'can add post', 'can delete post', 'can ban user'
    ]):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

adm = Admin('passion', 'Zz')
adm.show_privileges()
