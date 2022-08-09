"""
@creat_time 2022/8/9 15:09
@creat_by PassionZz
@file_name 10-12
@description 记住喜欢的数字
"""
import json


def get_number():
    file_name = 'favorite_number.json'
    try:
        with open(file_name) as file:
            number = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return number


def greet():
    favorite_number = get_number()
    if favorite_number:
        print("I know your favorite number! It's " + favorite_number)
    else:
        number = input("Please enter your favorite number: ")
        file_name = 'favorite_number.json'
        with open(file_name, 'w') as file:
            json.dump(number, file)
            print("stored!")


greet()
