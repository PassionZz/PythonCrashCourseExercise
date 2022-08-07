"""
@creat_time 2022/8/7 17:19
@creat_by PassionZz
@file_name restaurant
@description 
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

