"""
@creat_time 2022/8/6 14:10
@creat_by PassionZz
@file_name 7-3
@description 10的整数倍
"""
num = input("Please enter a number ")
num = int(num)
if num % 10 == 0:
    print("It is a Mutiple of 10!")
else:
    print("It isn't a Mutiple of 10!")