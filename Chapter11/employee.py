"""
@creat_time 2022/8/9 17:07
@creat_by PassionZz
@file_name employee
@description 
"""


class Employee():
    """雇员类"""

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, increase=5000):
        self.salary += increase
