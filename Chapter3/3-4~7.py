"""
@creat_time 2022/7/27 15:44
@creat_by PassionZz
@file_name 3-4
@description 
"""
invite_list = ['Kobe','Lebron','Joy','Sana']
for name in invite_list :
    print("Hi! " + name + ", I'll have a party tonight,come join us!")
#3-5
print('----')
print("Sana Can't get us")
invite_list[-1] = 'Winter'
for name in invite_list :
    print("Hi! " + name + ", I'll have a party tonight,come join us!")
#3-6
print('----')
print("I got a bigger table")
invite_list.insert(0,'Irene')
invite_list.insert(2,'Lisa')
invite_list.append('noze')
for name in invite_list :
    print("Hi! " + name + ", I'll have a party tonight,come join us!")
#3-7
print('----')
print("sry, I can just invite two of you")
while len(invite_list) >2 :
    name = invite_list.pop()
    print("sry, " + name + " I can't get you here!")
for name in invite_list :
    print("Hi," + name +" you're still invited!")
print(invite_list)
del invite_list[0]
del invite_list[0]
print(invite_list)
