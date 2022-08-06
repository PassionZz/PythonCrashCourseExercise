"""
@creat_time 2022/8/6 20:44
@creat_by PassionZz
@file_name 9-5
@description 尝试登录次数
"""


class User():
    """用户类"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + " "+ self.last_name.title() )

    def greet_user(self):
        print("Hello,"+ self.first_name+" "+self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


usr = User('passion', "Z")
usr.increment_login_attempts()
usr.increment_login_attempts()
usr.increment_login_attempts()
print(usr.login_attempts)

usr.reset_login_attempts()
print(usr.login_attempts)
