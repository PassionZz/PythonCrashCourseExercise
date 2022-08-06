"""
@creat_time 2022/8/5 21:20
@creat_by PassionZz
@file_name 5-11
@description 序数
"""
numbers = list(range(1,10))
for num in numbers :
    print(num)
    if num == 1:
        print('1st')
    elif num ==2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(str(num)+'th')
