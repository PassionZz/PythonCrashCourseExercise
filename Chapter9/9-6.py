"""
@creat_time 2022/8/7 14:58
@creat_by PassionZz
@file_name 9-6
@description 冰淇淋小店
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


class IceCreamStand(Restaurant):
    """冰淇淋店  """
    def __init__(self, restaurant_name, cuisine_type, flavors=['vanilla', 'chocolate']):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_ice_cream(self):
        msg = "We got this kinds of IceCream "
        msg += str(self.flavors)
        print(msg)


dq = IceCreamStand('DQ', 'ice cream')
dq.show_ice_cream()