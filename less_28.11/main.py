# N = int(input('Введите число N... '))
# S = 1
# if N == 0:
#     print('Нельзя использовать ноль!')
# elif N < 0:
#     N *= (-1)
#     for i in range(1, N):
#         S = S + round((1 + 1 / N) ** N, 0)
#         print(i , ' = ' , S, end=' , ')
#     print(N , ' = ' , S + round((1 + 1 / N) ** N, 0))
# else:
#     for i in range(1, N):
#         S = S + round((1 + 1 / N) ** N, 0)
#         print(i , ' = ' , S, end=' , ')
#     print(N , ' = ' , S + round((1 + 1 / N) ** N, 0))

# import random
# n = int(input())
# mult = 1
# some_list = [random.randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('file.txt', 'w+', encoding='utf-8') as file:
#     count = random.randint(1, n)
#     for _ in range(count):
#         file.write(f'{random.randint(0, n - 1)}' + '\n')
#     file.seek(0, 0)
#     index_list = file.read().splitlines()
#     for index in index_list:
#         mult = mult * some_list[int(index)]
# print(mult)


# a = int(input('Ввод числа '))


# with open('file.txt', 'w', encoding='utf-8') as file:
#     for _ in range(a):
#         file.write(input() + '\n')

# c = input('Введите искомое ')

# with open('file.txt', 'r', encoding='utf-8') as file:

#     strings = file.read().splitlines()

#     count = 0
#     b = False
#     for line in strings:
#         count += 1
#         if c in line:
#             b = True
#             print(f'DA ->  {count}')

#     if not b:
#         print('NET')


# Напишите функцию, которая принимает номер месяца и язык (русский или английский), а возвращает его название.
#            Ввод:
#               print(month_name(3, "en"))
#               March
#            Ввод
#               print(month_name(3, "ru"))
#               март

# def mounth(x, y):
#     listEn = ('January', 'February', 'March', 'April', 'May', 'June',
#               'July', 'August', 'September', 'October', 'November', 'December')
#     listRu = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
#               'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
#     if x  > 0 and x < 13:
#      if y == 'en':
#          return listEn[x-1]

#      if y == 'ru':
#          return listRu[x-1]

# print(mounth(31,'en'))


# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет
# ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe'] -> ответ 3

# some_list = ['qwe', 'asd', 'zxc', 'z', 'ertqwe']

# a = input('Введите искомое ')

# count = 0
# count2 = 0
# b = False
# for line in some_list:
#     count += 1
#     if a == line:
#         count2 += 1
#         if count2 == 2:
#             b = True
#             print(f'{count}  ')
#             break
# if not b:
#     print('-1')


# # list
# some_list = [1, 2, 3, 2, 0, 'fgd', True]
# print(f'{some_list} - список')

# #tuple
# some_tuple = tuple(some_list)
# some_tuple2 = (3, 54, 83, 832)
# print(some_tuple, some_tuple2, 'кортежи')

# #set
# some_set = set(some_list)
# some_set2 = {2, 3, 4, 9, 10}
# some_set2.add(8)
# some_set2.remove(3)

# #frozenset
# some_frozenset = frozenset(some_set)
# some_frozenset2 = frozenset((3, 4, 5, 10))

# #dict
# some_dict = {1: True, 2: 'second'}
