"""
@creat_time 2022/8/6 18:15
@creat_by PassionZz
@file_name 8-14
@description 汽车
"""


def build_car(builder, model, **car_info):
    car_profile = {'builder': builder,
                   'model': model}
    for key, value in car_info.items():
        car_profile[key] = value
    return  car_profile


car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)