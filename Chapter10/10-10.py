"""
@creat_time 2022/8/9 13:57
@creat_by PassionZz
@file_name 10-10
@description 常见单词
"""
file_name = 'Mrs.Dalloway.txt'
with open(file_name) as dalloway:
    article = dalloway.read()
    print(article.count('the'))