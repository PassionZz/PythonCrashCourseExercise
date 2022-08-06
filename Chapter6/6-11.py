"""
@creat_time 2022/8/6 10:54
@creat_by PassionZz
@file_name 6-11
@description 城市
"""
cities = {
    'Beijing': {
        'Country': 'CHN',
        'popularity': '21,000,000',
        'others': '2022 Winter Olympics'
    },
    'NewYork': {
        'Country': 'USA',
        'popularity': '8,620,000',
        'others': 'Nets and knicks'
    },
    'Tokyo': {
        'Country': 'Japan',
        'popularity': '12,990,000',
        'others': '2020 Olympics'
    },
}
for city, dic in cities.items():
    print(city)
    print(dic)