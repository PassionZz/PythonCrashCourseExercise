"""
@creat_time 2022/8/4 20:21
@creat_by PassionZz
@file_name 4-11
@description 你的披萨和我的披萨
"""
pizzas = ['bacon pizza','tomato pizza','cheese pizza','Sea food','chicken pizza']
# for pizza in pizzas :
#     print(pizza)
friend_pizzas = pizzas[:]

pizzas.append('durian pizza')
friend_pizzas.append('beef pizza')

print("My favourite pizzas are: " )
for pizza in pizzas:
    print(pizza)

print("My friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)