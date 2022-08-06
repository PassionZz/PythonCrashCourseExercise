"""
@creat_time 2022/8/6 10:01
@creat_by PassionZz
@file_name 6-5
@description 河流
"""
rivers = {
    'Nile': 'egypt',
    'Amazon': 'USA',
    'Changjiang': 'CHN'
}
for river, nation in rivers.items():
    print('the '+river + ' runs through ' + nation)

for river in rivers.keys():
    print(river)

for nation in rivers.values():
    print(nation)