"""
@creat_time 2022/8/6 17:18
@creat_by PassionZz
@file_name 8-7
@description 专辑
"""


def make_album(singer, album_name, count_song=0):
    if count_song == 0:
        return {'singer': singer, 'album_name': album_name}
    else:
        return {'singer': singer, 'album_name': album_name, 'count_song': count_song}


dic = make_album('Jay', "最伟大的作品", 6)
print(dic)

dic = make_album('JJ', '可惜没如果')
print(dic)

dic = make_album('Pharaoh', '我想')
print(dic)
