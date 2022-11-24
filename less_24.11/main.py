# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 

# a = int(input())
# res = 3
# list = []
# for a in  range(0,a-1):
#     if a%2 == 0:
   
#          list.append( res**a)
#     else:
#        list.append( res**a * - 1  )
# print(list)

# ----------------------


# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# a = int(input())
# list = []
# for _ in range(1,a+1):
#     list.append(3*_+1)
# print(list)


# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# a = 'Метод str.count() возвращает количество вхождений подстроки sub в строку str в диапазоне индексов [start, end], если они переданы в метод.'
# b = str(input())
# print(a.count('str'))
# c  = 0

# list = a.split(' ')

# s1 = input()
# s2 = input()
# if s1 < s2:
#     s2, s1 = s1, s2
# ind = 0
# c = 0
# while ind < len(s1):
#     if s1[ind: ind + len(s2)] == s2:
#         c += 1
#         ind += len(s2)
#     else:
#         ind += 1
# print(c)
# s1 = input()
# s2 = input()
# if s1 < s2:
#     s2, s1 = s1, s2
# ind = 0
# c = 0
# while ind < len(s1):
#     if s1[ind: ind + len(s2)] == s2:
#         c += 1
#     else:
#         ind += 1
# print(c)

# s1 = input()
# s2 = input()
# print(s1.count(s2) or s2.count(s1))

