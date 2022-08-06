"""
@creat_time 2022/8/6 15:32
@creat_by PassionZz
@file_name 7-8
@description 熟食店
"""
sandwich_orders = ['chicken sandwich', 'beef sandwich', 'egg sandwich']
finished_sanwiches = []
while sandwich_orders:
    cur_sandwich = sandwich_orders.pop()
    print("I make your "+cur_sandwich+"!")
    finished_sanwiches.append(cur_sandwich)
print(finished_sanwiches)