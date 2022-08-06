"""
@creat_time 2022/8/6 14:27
@creat_by PassionZz
@file_name 7-4
@description 比萨配料
"""
prompt = "Plese enter your pizza toppings: "
prompt += "\n(enter 'quit' to end the program) "

msg = ""
while msg != 'quit':
    msg = input(prompt)
    if msg != 'quit':
        print("we'll add "+msg)