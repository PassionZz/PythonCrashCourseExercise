"""
@creat_time 2022/8/6 18:12
@creat_by PassionZz
@file_name 8-13
@description 
"""


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


# profile = build_profile('Shawn', 'Zhang', gender='男', city='Guangzhou')
# print(profile)