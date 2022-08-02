"""
@creat_time 2022/8/2 16:28
@creat_by PassionZz
@file_name 4-5
@description 计算1～1000000的总和
"""
import time

numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
pre = time.time()
all = sum(numbers)
print(time.time()-pre)
print(all)