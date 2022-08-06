"""
@creat_time 2022/8/5 21:13
@creat_by PassionZz
@file_name 5-10
@description 检查用户名
"""
current_users = ['passionzz', 'yikofish', 'clozechair', 'admin', 'mlisn']
new_users = ['courtman', 'passionZz', 'yikofish', 'longlongway', 'spicehot']

for user in new_users:
    if user.lower() in current_users:
        print("you need another name")
    else:
        print("this name is avaliable!")