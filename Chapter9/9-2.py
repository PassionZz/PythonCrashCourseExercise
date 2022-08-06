"""
@creat_time 2022/8/6 20:15
@creat_by PassionZz
@file_name 9-2
@description 三家餐馆
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


fri_res = Restaurant('omasak', 'nono')
sec_res = Restaurant('susi', 'nood')
third_res = Restaurant('lanzhou', 'lamian')

fri_res.describe_restaurant()
sec_res.describe_restaurant()
third_res.describe_restaurant()