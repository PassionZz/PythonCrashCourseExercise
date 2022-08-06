"""
@creat_time 2022/8/5 21:06
@creat_by PassionZz
@file_name 5-8
@description 以特殊方式跟管理员打招呼
"""
users = ['passionzz', 'yikofish', 'clozechair', 'admin', 'mlisn']
for user in users:
    if user == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello "+ user +",thank you for logging in again")