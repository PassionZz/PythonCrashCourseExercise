"""
@creat_time 2022/8/6 17:12
@creat_by PassionZz
@file_name 8-6
@description 城市名
"""


def city_country(name, country):
    combine = name + ',' + country
    return combine.title()


msg = city_country('TOkyo', 'Japan')
print(msg)

msg = city_country('Seoul', 'KoREan')
print(msg)

msg = city_country('BeijinG', 'ChIna')
print(msg)