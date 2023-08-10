# Problem 1
#
# def add(a, b):
#     return a + b
#
# def substract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     return a / b
#
# a = int(input('Write your first number - '))
# b = int(input('Write your second number - '))
#
# x = substract(a, b)
# print(f'Your answer is - {x}')


# Problem 2
#
# def count_text(text):
#     count = 0
#     for i in text:
#         count += 1
#     return count
#
# x = input('Write your text - ')
#
# a = count_text(x)
# print(a)


# Problem 3
#
# def concatenate_dict(dict_1, dict_2):
#     a = dict_1|dict_2
#     return a
#
# a = {'Name': 'Matvey'}
# b = {'Age': 21}
#
# x = concatenate_dict(a, b)
# print(x)


# Problem 4
#
# def menu(text):
#     with open('/Users/cer6erus7/Desktop/menu.txt', "w") as f:
#         f.write(text)
#     return f
#
# t = input('Type your menu - ')
#
# t = menu(t)
# print(t)


# Problem 5
#
# def file_name(name):
#     with open(name, 'w') as f:
#         f.write('')
#     return f
#
# a = input("Write name of file - ")
#
# t = file_name(a)
# print(t)


# Problem 6
#
# def fun():
#     print('Я главная функция.')
#     def fun_1():
#         print('Я вложенная функция.')
#     fun_1()
#
# fun()


# Problem 7
#
# def dicttuple(dict):
#     a = tuple(dict.keys())
#     b = tuple(dict.values())
#     return a, b
#
# lol = {'Name': 'Matvey', 'Age': 21}
#
# print(dicttuple(lol))
#

# Problem 8
#
# def get_prime_numbers(number):
#     for i in range(2, number):
#         if number % i == 0:
#             print('not prime!')
#             break
#     else:
#         print('prime')
#
# nu = int(input('Type your number - '))
#
# get_prime_numbers(nu)


# problem 9
#
# def lst(*args):
#     a = list(args)
#     return a
#
# l1 = 13
# l2 = 'dqw'
# l3 = ('dawda', 23)
# l4 = ['das', 25]
#
# x = lst(l1, l2, l3, l4)
#
# print(x)
# print(type(x))


# Problem 10
#
# def typing(number):
#     for i in range(1, number):
#         a = str(number)
#         strings = a * number
#
#     return strings
#
# n = int(input('Type your number - '))
#
# x = typing(n)
# print(x)
# print(type(x))

##############################################################
#
# def typing(number):
#
#     lst = []
#     for i in range(number):
#         lst.append(str(number))
#     print(' '.join(lst))
#
#     return str(lst)
#
# n = int(input('Type your number - '))
#
# x = typing(n)
# print(type(x))


# Problem 11
#
# def name_salary(name, salary):
#     try:
#         if salary == '':
#             salary = 5000
#         output = f"{name} - {int(salary)}"
#         print(output)
#
#     except:
#         print('\nYou need to write the number, not words!')
#
# n = input('Print your name - ')
# s = input('Print your salary - ')
#
# name_salary(n, s)


# Problem 12
#
# def lsit(n):
#     lol = []
#     lol.append(str(n))
#     lol.append(n)
#     lol.append(bool(n))
#     lol.append([n])
#     lol.append(float(n))
#
#     return lol
#
# number = int(input("Print your number - "))
#
# x = lsit(number)
# print(x)
