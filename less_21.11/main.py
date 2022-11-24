# num1, num2 = map(int, input().split(', '))
# if num1 ** 2 == num2 or num2 ** 2 == num1:
#     print('да')
# else:
#     print('нет')

# maxx = int(input())
# for _ in range(4):
#     n = int(input())
#     if n > maxx:
#         maxx = n
# print(maxx)


# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# N = int(input())
# numbers = []
# for s in range(-N , N + 1):
#     numbers.append(s)
# print(numbers)

# num = int(input())

# for i in range( -num) :
#     print(int(i))


# print(int(float(input())*10%10) )


# num = int(input())
# if (num%5 == 0 or num %10 or num%15) and num%30 != 0:
#     print('yes')
# else:
#     print('no')


# n = int(input())
# # if n > 0:
# #     for i in range(-n, n):
# #         print(i, end=', ')
# #     print(n)
# # else:
# #     for i in range(-n, n, -1):
# #         print(i, end=', ')
# #     print(n)


# n = int(input())
# print(*list(range(-n, n + 1)), sep=', ')



# some_str = input()
# if ',' in some_str:
#     ind = some_str.index(',')
#     print(some_str[ind + 1])
# else:
#     print('нет')
# some_str = input()
# if ',' in some_str:
#     some_list = some_str.split(',')
#     print(some_list[1][0])
# else:
#     print('нет')

# number = float(input())
# if number % 1 != 0:
#     number = number * 10
#     number = int(number)
#     print(number % 10)
# else:
#     print('нет')

for i in range(12231,1,-11):
    print(i)
