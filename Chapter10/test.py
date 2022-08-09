"""
@creat_time 2022/8/9 09:01
@creat_by PassionZz
@file_name test
@description chapter10 file
"""
import json

# number = [1, 24, 50, 2.14, 22, 4403]
file_name = 'numbers.json'
with open(file_name) as f_obj:
    # json.dump(number, f_obj)
    number = json.load(f_obj)
print(number)