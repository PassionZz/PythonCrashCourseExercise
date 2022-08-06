"""
@creat_time 2022/8/6 17:25
@creat_by PassionZz
@file_name 8-8
@description 用户的专辑
"""


def make_album(singer, album_name, count_song=0):
    if count_song == 0:
        return {'singer': singer, 'album_name': album_name}
    else:
        return {'singer': singer, 'album_name': album_name, 'count_song': count_song}


while True:
    singer = input("Please Enter Singer's name: ")
    album = input("Album name: ")
    if singer == 'q' or album == 'q':
        break
    dic = make_album(singer, album)
    print(dic)