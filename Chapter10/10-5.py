"""
@creat_time 2022/8/9 11:57
@creat_by PassionZz
@file_name 10-5
@description 关于编程的调查
"""
file_name = 'reason_for_programming.txt'
with open(file_name, 'a') as file:
    while True:
        reason = input("What's the reason you wanna programming?:")
        if reason == 'quit':
            break
        file.write('\n' + reason)
