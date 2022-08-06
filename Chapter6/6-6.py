"""
@creat_time 2022/8/6 10:08
@creat_by PassionZz
@file_name 6-6
@description 调查
"""
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
investigate = ['sarah', 'sid', 'kat']
for name in investigate:
    if name in favourite_languages.keys():
        print('thanks for you participant')
    else:
        print('invitation')