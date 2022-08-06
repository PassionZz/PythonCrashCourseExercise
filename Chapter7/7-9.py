"""
@creat_time 2022/8/6 15:35
@creat_by PassionZz
@file_name 7-9
@description 五香烟熏牛肉卖完了
"""
sandwich_orders = ['chicken sandwich', 'pastrami', 'beef sandwich', 'pastrami', 'egg sandwich', 'pastrami']
print('pastrami has beeb sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
