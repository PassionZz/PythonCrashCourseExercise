"""
@creat_time 2022/8/6 20:17
@creat_by PassionZz
@file_name 9-3
@description 用户
"""


class User():
    """用户类"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name.title() + " "+ self.last_name.title() )

    def greet_user(self):
        print("Hello,"+ self.first_name+" "+self.last_name)

user_1 = User('shawn', 'zhang')
user_1.describe_user()
user_1.greet_user()
user_2 = User('alva', 'lin')
user_2.describe_user()
user_2.greet_user()
user_3 = User('Kobe', 'bryant')
user_3.describe_user()
user_3.greet_user()