"""
@creat_time 2022/8/6 14:39
@creat_by PassionZz
@file_name 7-6
@description 电影票
"""
prompt = "Please enter your age: "
"""使用break语句
while True:
    age = input(prompt)
    if not age.isdigit() : #isdigit()方法用于判断输入的字符串是否为纯数
        break
    age = int(age)
    if age < 3:
        print('free!')
    elif 3 <= age < 12:
        print('$10,please!')
    elif age >= 12:
        print('$15,please!')
"""
""" while使用条件判断
age = input(prompt)
while age.isdigit():
    age = int(age)
    if age < 3:
        print('free!')
    elif 3 <= age < 12:
        print('$10,please!')
    elif age >= 12:
        print('$15,please!')
    age = input(prompt)
"""
# 使用标志
active = True
while active:
    age = input(prompt)
    if  age.isdigit():
       age = int(age)
       if age < 3:
           print('free!')
       elif 3 <= age < 12:
           print('$10,please!')
       elif age >= 12:
           print('$15,please!')
    else:
        active = False