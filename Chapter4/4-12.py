"""
@creat_time 2022/8/4 20:29
@creat_by PassionZz
@file_name 4-12
@description 使用多个循环
"""
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favourtie foods are:")
for food in friend_foods:
    print(food)