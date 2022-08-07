"""
@creat_time 2022/8/7 17:28
@creat_by PassionZz
@file_name 9-13
@description python3.6之后字典已经默认按照键的创建顺序来排序了，并非完全无序
"""
from collections import OrderedDict

programming_words = OrderedDict()
programming_words['list'] = '列表'
programming_words['int'] = '整型'
programming_words['string'] = '字符串'
programming_words['if-else'] = '判断'
programming_words['while'] = '循环'
programming_words['str'] = 'string'
programming_words['arraylist'] = '顺序表'
programming_words['LinkedList'] = '链表'
programming_words['isinstance'] = '类型判断'
for word, mean in programming_words.items():
    print(word + " mean: " + mean)