"""
@creat_time 2022/8/9 11:32
@creat_by PassionZz
@file_name 10-4
@description 访客名单
"""
import time

file_name = 'guest_book.txt'
with open(file_name, 'w') as f:
    while True:
        guest_name = input("Please enter your name: ")
        if guest_name == 'quit':
            break
        print("Welcome! " + guest_name)
        f.write('\n'+guest_name + " has logined in at " + time.asctime())