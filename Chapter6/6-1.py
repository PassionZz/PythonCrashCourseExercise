"""
@creat_time 2022/8/6 08:43
@creat_by PassionZz
@file_name 6-1
@description 人
"""
rg = {'first_name': 'Gren', 'last_name': 'Xu', 'age': 22, 'city': 'GuangZhou'}
print(rg)
for item in rg:
    if isinstance(rg[item], int): #使用isinstance()判断类型
        print(item+':'+str(rg[item]))
    else:
        print(item+':'+rg[item])
