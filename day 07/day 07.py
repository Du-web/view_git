# name = input('>>>>>')
# age = input('<<<<<')
# print('我是{{{{{0}}}}}，我今年{1}岁'.format(name,age))
'''
6. 写一个密码级别检测的程序
低级密码：由纯数字或字母组成，长度低于8位
中级密码：由数字，字母或特殊符号两种及以上的任意组合，密码长度为8-15位
高级密码：必须由数字，字母和特殊符号三种组合，密码长度不低于16位
说明：用户输入密码，会输出验证密码是什么级别的信息。其中密码输入后会额外提示：
1. 当密码为空，提示不能为空
2. 当密码以数字开头，提示不能以数字开头
3. 当密码长度和组合不够高级密码要求，要提示正确的长度及组合
'''

# symbols = '~!@#$%^&*()_=-/,.?<>;:[]{}\|'
# letters = 'abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXZ'
# nums = '0123456789'
# t = 'y'
# while t:
#     print('请输入您要检验的密码:')
#     password = input()
#     lenght = len(password)
#     while password.isspace() or lenght == 0:
#         password = input('输入的密码不能为空，请重新输入')
#         lenght = len(password)
# #判断长度
#     if lenght <= 8:
#         flag_len = 1
#     elif 8 < lenght < 16:
#         flag_len = 2
#     else:
#         flag_len = 3
# #判断是否有数字
#     flag_con = 0
#     for each in password:
#         if each in nums:
#             flag_con += 1
#             break
# #判断是否有字母
#     for each in password:
#         if each in letters:
#             flag_con += 1
#             break
# #判断是否有特殊符号
#     for each in password:
#         if each in symbols:
#             flag_con += 1
#             break
#     while 1:
#         print('您要检测的密码等级为:')
#         if flag_len == 1 or flag_con == 1:
#             print('低')
#         elif flag_len == 2 or flag_con == 2:
#             print('中')
#         else:
#             print('高')
#             break
#         print('''请按以下方式提升您的密码安全级别：
#     1.密码必须由数字、字母及特殊字符三种组合
#     2.密码只能由字母开头
#     3.密码长度不能低于16位
#         ''')
#         break
#     t = input('还要测试么（“y”继续，其他退出)')

# import random
#
# random.sample()

# import string
# print(list(zip((10,20,30),(40,55,60))))
# dict1 = {}
# print(dict1.fromkeys([1,2,3],(1,2)))
# set1 = {{1:'a'}}
# print(set1)
print(type(('abc',)))