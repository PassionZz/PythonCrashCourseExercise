"""
@creat_time 2022/8/9 10:10
@creat_by PassionZz
@file_name 10-1
@description Python学习笔记
"""
file_name = 'learning_python.txt'
with open(file_name) as file:
    # contents = file.read()
    # print(contents)

    # for line in file.readlines():
    #     print(line.strip())

    lines = file.readlines()
for lin in lines:
    print(lin.strip())