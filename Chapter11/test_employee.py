"""
@creat_time 2022/8/9 17:09
@creat_by PassionZz
@file_name test_employee
@description 
"""
import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """Employee类的测试"""

    def setUp(self):
        self.employ = Employee('passionzz', "Zhang", 10000)

    def test_give_default_raise(self):
        self.employ.give_raise()
        self.assertEqual(self.employ.salary, 15000)

    def test_give_custom_raise(self):
        self.employ.give_raise(10000)
        self.assertEqual(self.employ.salary, 20000)


if __name__ == '__main__':
    unittest.main()
