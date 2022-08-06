"""
@creat_time 2022/8/6 20:39
@creat_by PassionZz
@file_name 9-4
@description 就餐人数
"""


class Restaurant():
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print("opening")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, increse):
        self.number_served += increse

res = Restaurant('ningning', 'idol')
print(res.number_served)
res.number_served = 2
print(res.number_served)

res.set_number_served(4)
print(res.number_served)

res.increment_number_served(8)
print(res.number_served)