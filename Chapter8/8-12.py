"""
@creat_time 2022/8/6 18:02
@creat_by PassionZz
@file_name 8-12
@description 三明治
"""


def make_sanwich(*ingredients):
    print("\nMaking a sandwich with :")
    for ingredient in ingredients:
        print("- "+ ingredient)


make_sanwich('bacon', 'egg')
make_sanwich('beef', 'egg', 'vegetables')
make_sanwich('nothing')