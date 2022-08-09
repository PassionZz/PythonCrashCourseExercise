"""
@creat_time 2022/8/9 14:44
@creat_by PassionZz
@file_name 10-11
@description 喜欢的数字
"""
import json


def remember_favorite_number():
    """存储用户最喜欢的数字"""
    number = input("What's your favorite number: ")
    file_name = 'favorite_number.txt'
    with open(file_name,'w') as file:
        json.dump(number, file)

def get_favorite_number():
    """获取最喜欢的数字"""
    file_name = 'favorite_number.txt'
    with open(file_name) as file:
        number = json.load(file)
    return number

remember_favorite_number()
print("I know your favorite number! It's "+get_favorite_number())