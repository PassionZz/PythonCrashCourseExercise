"""
@creat_time 2022/8/9 13:49
@creat_by PassionZz
@file_name 10-8
@description 猫和狗
"""
file_name = ['cats.txt', 'dogs.txt']
for file in file_name:
    try:
        with open(file) as f:
            contents = f.read()
            print(contents.strip())
    except FileNotFoundError:
        print("Can's find file " + file)
