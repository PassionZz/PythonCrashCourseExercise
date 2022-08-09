"""
@creat_time 2022/8/9 15:21
@creat_by PassionZz
@file_name 10-13
@description 
"""
import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username,f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        verify = input("Are your " + username + " ?(y/n)")
        if verify == 'n':
            username = get_new_user()
            print("We'll remember you when you come back, " + username +" !")
        else:
            print("Welcome back, "+ username +' !')
    else:
        username = get_new_user()
        print("We'll remember you when you come back, " + username + " !")
greet_user()




