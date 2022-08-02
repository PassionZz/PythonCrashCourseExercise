"""
@creat_time 2022/8/2 16:36
@creat_by PassionZz
@file_name 4-8
@description 立方
"""
# numbers= []
# for value in range(1,11):
#     numbers.append(value**3)

numbers = [value**3 for value in range(1,11)]

for num in numbers:
    print(num)