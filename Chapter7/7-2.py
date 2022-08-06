"""
@creat_time 2022/8/6 14:02
@creat_by PassionZz
@file_name 7-2
@description 餐馆订位
"""
count  = input("How many people need to eat?")
count = int(count)

if count > 8:
    print("We ain't got spare table")
else:
    print("We have your table!")