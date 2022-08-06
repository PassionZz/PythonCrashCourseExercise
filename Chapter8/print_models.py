"""
@creat_time 2022/8/6 19:26
@creat_by PassionZz
@file_name print_models
@description 
"""
import printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)