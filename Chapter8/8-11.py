"""
@creat_time 2022/8/6 17:33
@creat_by PassionZz
@file_name 8-11
@description 了不起的魔术师
"""


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    result_list = []
    while magicians:
        cur = magicians.pop()
        cur = 'the Great ' + cur
        result_list.append(cur)
    magicians = result_list[:]
    return magicians

lis = ['david', 'andy', 'Fridy', 'pepper']
show_magicians(lis)
result = make_great(lis[:])
print()
show_magicians(lis)
print()
show_magicians(result)