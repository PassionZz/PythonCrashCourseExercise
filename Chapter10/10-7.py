"""
@creat_time 2022/8/9 13:41
@creat_by PassionZz
@file_name 10-7
@description 加法计算器
"""
flag = 0
num_sum = 0
while True:
    num = input("Please enter your number: ")
    try:
        num_sum += int(num)
    except ValueError:
        print("wrong value,please enter a number: ")
    else:
        flag += 1
        if flag == 2:
            break
print("sum= " + str(num_sum))