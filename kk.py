# lis = [5, 4, 3, 2, 1]
# for i in range(len(lis) - 1):
#     for j in range(len(lis) - i - 1):
#         if lis[j] > lis[j + 1]:
#             lis[j], lis[j + 1] = lis[j + 1], lis[j]
# print(lis)

# for i in range(len(lis)):
#     for j in range(i + 1, len(lis)):
#         if lis[i] > lis[j]:
#             lis[i], lis[j] = lis[j], lis[i]
# print(lis)


# with open('poem.txt', 'w', encoding='utf8') as f:
#     print('请输入写入的内容【按“:w”退出】:')
#     while True:
#         a = input()
#         try:
#             f.write(f'{a}\n')
#             if a == ':w':
#                 raise KeyboardInterrupt
#         except KeyboardInterrupt:
#             print('退出书写')
#             break
import time

# def count_time(fn):
#     def inner():
#         now = time.time()
#         fn()
#         end = time.time()
#         print(f'时长为：{end - now}')
#
#     return inner
#
#
# @count_time
# def sum_fn():
#     sum1 = 0
#     for i in range(10000):
#         sum1 += i
#     print(sum1)
#
#
# sum_fn()

# def remove_fn(obj):
#     s1 = set(obj)
#     print(list(s1))
#
#
# lis = [1, 3, 1, 4, 5, 2, 1]
# remove_fn(lis)


# class Worker:
#     age = 18
#
#     def __init__(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     n = property(get_age)
#
#
# w = Worker(25)
# # w.set_age(26)
# print(w.n)

# t1 = ('a', 'b', 'c', 'd', 'e')
# t2 = (1, 2, 3, 4, 5)
# res = dict(zip(t1, t2))
# print(res)

# s = 'HelloMyWorld'
# lenght = len(s)
# for i in range(1, lenght):
#     if s[i].isupper():
#         s = s.replace(s[i], ' ' + s[i].lower())
# print(s)

# def fn(s):
#     lenght = len(s)
#     for i in range(1, lenght):
#         if s[i].isupper():
#             s = s.replace(s[i], ' ' + s[i].lower())
#     return s
#
#
# str1 = 'HelloMyWorld'
# print(fn(str1))

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j} * {i} = {i * j}\t', end=' ')
#     print()

import threading
class LeapYear(threading.Thread):

    def __init__(self, y):
        super().__init__()
        self.year = y

    def run(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
            print(f'{self.year}是闰年')
        else:
            print(f'{self.year}不是闰年')


def isprime(num):
    flag = True
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            flag = False
            break
    if flag:
        print(f'{num}是质数')
    else:
        print(f'{num}不是质数')


# if __name__ == '__main__':
#
#     year = int(input('请输入年份:'))
#     num = int(input('请输入一个数:'))
#     t1 = LeapYear(year)
#     t2 = threading.Thread(target=isprime, args=(num,))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()


def count_fn(s):
    con_lit = 0
    con_dig = 0
    con_oth = 0
    for i in s:
        if i.isalpha():
            con_lit += 1
        elif i.isdigit():
            con_dig += 1
        else:
            con_oth += 1
    print(f'字符"{s}"中，共有英文字符{con_lit}个，数字{con_dig}个，其他字符{con_oth}个')


str1 = input('请输入一串字符:')
count_fn(str1)

