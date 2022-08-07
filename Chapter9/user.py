"""
@creat_time 2022/8/7 17:21
@creat_by PassionZz
@file_name user
@description 
"""


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

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

