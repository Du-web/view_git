# for i in range(6):
#     for j in range(5):
#         print(str(i) + ':' + str(j),end=' ')

# lis = [1,2,3]
# lis[2] = 5
# print(lis)

# import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# import this

# dic = {1:'a',2:'b'}
# print(dic.pop(3,None))

# def MyFun(x,y):
#     return x[0] * x[1] - y[0] * y[1]
#
# num = MyFun((3,4),(1,2))
# print(num)

import random

# print([i * 5 for i in range(1,10) if i%2])
# lis = [random.randint(10,20) for i in range(4)]
# print(lis)
# dic = {k:v for k,v in ['12',('name','python')]}
# dic = {i:0 for i in range(6)}
# print(dic)
# set1 = {random.randint(10,20) for i in range(6)}
# set1 = {pow(i,2) for i in range(5) if 1 % 2}
# print(set1)

# l1 = [1,2,3]
# # l2 = l1
# # l2 = l1.copy()
# l2 = l1[:]
# l1 = [[10,20],30]
# l2 = l1[:]
# l1[0][0] = 100
# print(l2)

# lis = [{'a':1,2:'v',3:'d'},{6:'o',7:'p',8:'k'}]
# # dic = {each for each in lis}
# for dic in lis:
#     if 'a' in dic:
#         print(dic['a'])
#         print(list(dic.values()))
#     print(len(dic))
#     dic.clear()
# print(lis)

# for i in range(4):
#     for j in range(5):
#         print('*'+ ' ',end=' ')
#     print()


# a= int(input('...'))
# b= int(input('...'))
# c = a
# while True:
#     if c % a == 0 and c % b == 0:
#         print(c)
#         break
#     c += 1

# def fn():
#     name = input('...')
#     return name
# fn()

# print(dict(a=1,b=2))
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(f'{j} * {i} = {i*j}',end='    ')
#     print(' ')


# def fn1():
#     def fn2():
#         a = 10
#         print(a)
#
#     return fn2
#
#
# rst = fn1()
# print(rst)
# rst()


# def sum_fn(*args, beas=3):
#     rst = 0
#     for i in args:
#         rst += i
#     return rst * beas
#
#
# # print(sum_fn(1, 2, 3, 4, 5))
# # print(sum_fn(1, 2, 3, 4, 5, beas=5))
#
#
# def num_fn():
#     print('所有水仙花数为:')
#     for i in range(100, 1001):
#         temp = i
#         sum1 = 0
#         while temp:
#             sum1 += (temp % 10) ** 3
#             temp //= 10
#         if sum1 == i:
#             print(i, end=' ')


# # num_fn()
# d1 = {'a': 1, 'b': 2, 'c': 3}
# for k in d1.values():
#     print(k)

# a = 10
# def fn(a):
#     a = 100
#     print(a)
# fn(a)
# print(a)


# dic = {'a':5,'g':6,'j':8, 1:'a'}
# if 'i' not in dic.keys():
#     print('i')
# print(len(dic))
# del dic['i']
# print(dic)
# rst = dic.items()
# print(rst)
# for k,v in rst:
#     print(k,type(k))
# # if 8 in dic.values():
# #     print('True')
# for i in dic:
#     print(i)


# s = 'abcdad'
# print(s.count('a'))

# import math
# math.dist(  cb   )
# f = open('1.txt', 'r')
# print(f.read(5))
# f.close()

# def fn():
#     a = 10
#     return a


# print(not 0 and 1 or 2 and 3 or 4)
# print({(1,2,3), fn()})
# l1 = ((x for x in range(10)))
# l1 = list((x for x in range(10)))
# l1 = list([x for x in range(10)])
# l1 = [x for x in range(10)]
# l1 = range(10)
# print(l1)
# for i in range(1,6):
#     print(i)
# n = 0
# while n < 5:
#     n += 1
#     print(i)

# lis = [5, 4, 3, 2, 1]
# for i in range(len(lis) - 1):
#     for j in range(len(lis) - i -1):
#         if lis[j] > lis[j + 1]:
#             lis[j], lis[j + 1] = lis[j + 1], lis[j]
# print(lis)
# try:
#     with open('poem.txt', 'w') as f:
#         a = input('请输入悯农【输入"W"退出】:\n')
#         while True:
#             if a != ':w':
#                 f.write(f'{a}\n')
#             else:
#                 break
# except UnboundLocalError as tip:
#     print(tip)

# print('请输入悯农【输入"W"退出】:\n')
# f = open('poem.txt', 'w', encoding='utf-8')
# while True:
#     a = input()
#     if a != ':w':
#         f.write(f'{a}\n')
#     else:
#         break
#
# f.close()

# print('请输入悯农【输入"W"退出】:\n')
# try:
#     with open('poem.txt', 'w', encoding='utf-8') as f:
#         while True:
#             a = input()
#             if a != ':w':
#                 f.write(f'{a}\n')
#             else:
#                 break
# except:
#     print('出错啦')

# s = 'HelloMyWorld'
# lis = list(s[1:])
# # print(lis)
# for i in lis:
#     if i.isupper():
#         i.lower()
# print(lis)
#         # lis.insert(lis.index(i), '')
# print(s[0] + str(lis))


# for i in range(1,10):
#     for j in range(i):
#         print(f'{j} * {i} = {j*i}', end=' ')
# print()


# for i in range(1999, 2021):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# val = float(input('请输入长度:'))
# unit = input('请输入单位:')
# if unit == 'in' or unit == '英寸':
#     print('%.2f英寸 = %.2f厘米' % (val, val * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%.2f厘米 = %.2f英寸' % (val, val % 2.54))
# else:
#     print('输入有误')

# for i in range(5):
#     print('*' * (i + 1))

# n = int(input('请输入行数：'))
# for i in range(n):
#     print(' ' * (n - i) + '*' * (i + 1), end=' ')
#     print()

# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     print("* " * i)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j} * {i } = {i *j}\t', end=' ')
#     print()

# set = {[1, 2, 3]}
# print(range(10))
print(sum(range(1, 10)))