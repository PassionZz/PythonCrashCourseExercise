"""
@creat_time 2022/8/7 17:51
@creat_by PassionZz
@file_name 9-14
@description 骰子
"""
from random import randint


class Die():
    """骰子类，使用1-6的随机数来确定die or not"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        num = randint(1, self.sides)
        print("---rolled----")
        if num == 6:
            print("-----Died!-----")


touzi_1 = Die()
flag = 1
for num in range(1, 11):
    touzi_1.roll_die()
    flag +=1
touzi_2 = Die(10)
for num in range(1, 11):
    touzi_2.roll_die()
    flag += 1
touzi_3 = Die(20)
for num in range(1, 11):
    touzi_3.roll_die()
    flag += 1
print(str(flag))