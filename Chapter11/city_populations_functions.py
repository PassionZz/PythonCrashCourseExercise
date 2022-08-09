"""
@creat_time 2022/8/9 16:04
@creat_by PassionZz
@file_name city_functions
@description 
"""


def get_formatted_city(city, country, population):
    msg = city.title() + "," + country.title() + " - " +population
    return msg
