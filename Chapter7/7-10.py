"""
@creat_time 2022/8/6 15:38
@creat_by PassionZz
@file_name 7-10
@description 梦想的度假胜地
"""
dream_places = {}
polling_active = True

while polling_active:
    name = input("what's your name: ")
    place = input("If you could visit one place in the world, where would you go? ")

    dream_places[name] = place

    repeat = input("quit?(y/n)")
    if repeat != 'n':
        polling_active = False

print("-----result----")
print(dream_places)