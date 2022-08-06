"""
@creat_time 2022/8/6 20:05
@creat_by PassionZz
@file_name 9-1
@description 餐馆
"""


class Restaurant():
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print("opening")


restaurant = Restaurant('omasake', 'susi')
restaurant.describe_restaurant()
restaurant.open_restaurant()