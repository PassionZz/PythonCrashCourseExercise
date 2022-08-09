"""
@creat_time 2022/8/9 10:19
@creat_by PassionZz
@file_name 10-2
@description C语言学习笔记
"""
file_name = 'learning_python.txt'
with open(file_name) as file:
    lines = file.readlines()
for line in lines:
    print(line.replace('Python', 'C').strip())
    # print(line.strip())