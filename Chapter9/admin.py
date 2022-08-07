"""
@creat_time 2022/8/7 17:24
@creat_by PassionZz
@file_name admin
@description 
"""
from user import User


class Privileges():
    """权限类，服务于管理员类"""
    def __init__(self, privileges=[
        'can add post', 'can delete post', 'can ban user'
    ]):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    """管理员类，用户类的子类"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

