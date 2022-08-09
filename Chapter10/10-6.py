"""
@creat_time 2022/8/9 13:27
@creat_by PassionZz
@file_name 10-6
@description 加法运算
"""
number = input("Please enter 2 numbers: ")
nums = number.split()
try:
    first = int(nums[0])
    second = int(nums[1])
except ValueError:
    print("Can't solve this value!")
else:
    sum = first + second
    print("sum: " + str(sum))
