"""
@creat_time 2022/8/9 16:04
@creat_by PassionZz
@file_name 11-1
@description 城市和国家
"""
import unittest
from city_populations_functions import get_formatted_city as cpf
from city_functions import  get_formatted_city as cf


class CityTestCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city(self):
        formatted_city = cf("santiago", "chile")
        self.assertEqual(formatted_city, 'Santiago,Chile')

    def test_city_country_population(self):
        formatted_city = cpf('santiago', 'chile', '5000000')
        self.assertEqual(formatted_city, 'Santiago,Chile - 5000000')


if __name__ == "__main__":
    unittest.main()
