# print('hello world')
# val = None
# print(type(val))
# a = 40
# b = 1.314
# print(a)
# print(type(b))
# s = 'hello \n world'
# print(s)

# print(a,' _ ',b,s)
# print(f'{a} - {b} - {s}')
# print('{} - {} - {}'.format(a,b,s))

# f = True
# print(type(f))
# print(f)

# print('Введите а')
# a = int(input())
# print('Введите б')
# b  = int(input())
# print(a,b,' ', a + b)

# a = 123
# b =-312
# c = a+b
# print(c)

# a = 1.3 
# b = 3
# c = a*b
# print(c)

# a = 1.31
# b = 3
# c = round(a*b,5)
# print(c)

# a = 3
# a +=5
# print(a)

################################## /
# логичиеские операции
################################## /
#  > , >=, <= , == , !=
#  not, and, or - не путатиь с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1+1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1,2]
# b = [1,2]
# print(a == b)

# a = 1 < 3  <5 < 10
# print(a)


# func = 1
# T = 4
# x = 123
# print(func < T> (x))

# f = 1 > 2 or 4 < 6
# print(f)


# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# f = [1,2,3,4]
# ## is_odd = f[0]%2 == 0
# is_odd = not f[0]%2 
# print(is_odd )

# Управляющие операторы if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b :
#     print(a)
# else:
#     print(b)


# username = input('Введите имя : ')
# if username == 'Маша':
#     print('Ура. это же маша')
# elif username == 'Марина':
#     print('Я так ждала вас. Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else :
#     print('Привет. ' , username)


# Циклы while и for

# original = 123
# inverted = 0
# while original !=0 :
#     inverted = inverted * 10 + (original%10)
#     original //= 10
# print(inverted)


# original = 123
# inverted = 0
# while original !=0 :
#     inverted = inverted * 10 + (original%10)
#     original //= 10
#     print(original)
# else: 
#     print('Пожалуй ')
#     print('хватит')
# print(inverted)


# for

# for i in  1,3,5,1 :
#     print(i**2)


# list =[1,2,3,4,5]
# for i in list :
#     print(i)

# r = range(10)
# for i in r :
#      print(i)

# for i in range(1,10,2):
#     print(i)


# for i in  'qqwerty' : 
#     print(i)


# Немоного о строках


# text = 'сьешь еще этих мягких французких булок'
# print(len(text))
# print('еще' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще','ЕЩЕ'))

# for c in text :
#     print(c.replace(c,c.upper()))

# text = 'сьешь еще этих мягких французких булок'   # справка по методу
# help(text.istitle)

# text = 'сьешь еще этих мягких французких булок'

# print(text[0])
# print(text[1])
# print(text[len(text)-1])
# print(text[-5])
# print(text[1:3])
# print(text[5:-11])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[0:3] + text[-5] + text[12] + text[0:1]
# print(text)


# Списки 

# numbers = [1,2,3,4,5]
# print(numbers)
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)
# numbers[0] = 10

# print(f'{len(numbers)} len')

# print(numbers)
# for i in numbers :
#     i*=2
#     print(i)



# color = ['red', 'green','blue']

# for e in color:
#     print(e)

# for e in color :
#     print(e*2)

# color.append('gray')
# print(color == ['red','green','blue','gray'])
# color.remove('red')

# Функции - это фрагмент программы, используемый многократно

def f(x):
    if x ==1 :
        return 'Целое'
    elif x == 2.3:
        return 23
    else :
        return

arg = 1
print(f(arg))
print(type(f(arg)))
arg = 2.3
print(f(arg))
print(type(f(arg)))
arg = '1'
print(f(arg))
print(type(f(arg)))

