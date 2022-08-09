"""
@creat_time 2022/8/9 11:29
@creat_by PassionZz
@file_name 10-3
@description 访客
"""
file_name = 'guest.ext'
with open(file_name, 'w') as file:
    guest_name = input("Please enter your name: ")
    file.write(guest_name)
