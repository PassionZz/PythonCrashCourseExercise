"""
@creat_time 2022/8/6 16:52
@creat_by PassionZz
@file_name 8-4
@description T恤
"""


def make_shirt(size='L', words='I love Python'):
    print("\nT恤的尺码为： " + size)
    print("需要打印的字样是：" + words)

make_shirt()
make_shirt('M')
make_shirt('S', 'F**k the world')