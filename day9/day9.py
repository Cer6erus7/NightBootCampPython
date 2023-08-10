# game "Multiplication"
#
# import random
#
# count_r = 0
# count_w = 0
# print('Напишите комманду "/exit" для завершения игры!\n')
#
# while True:
#     try:
#         max_value = input("Напишите лимит числа в игре - ")
#
#         if max_value == '/exit'.lower():
#             print(f'''
# Правильных ответов: {count_r}
# Неправильных ответов: {count_w}
#
# Хорошего вам дня!''')
#             break
#
#         max_value = int(max_value)
#         first_number = random.randint(0, max_value)
#         second_number = random.randint(0, max_value)
#
#         answer = int(input(f'{first_number} * {second_number}. Сколько будет? '))
#         i = first_number * second_number
#
#         if i == answer:
#             print('Молодец! Правильно!')
#             count_r += 1
#         else:
#             print('Не правильно!')
#             count_w += 1
#
#     except:
#         print('Вводите только числа!')


# Problem 1
#
# import my_modul
# my_modul


# Problem 2
#
# from random import choice
#
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# name_1 = []
#
# for i in range(4):
#     name_1.append(choice(names))
# print(name_1)


# Problem 3
#
# import sys
# print(sys.platform)


# Problem 5
#
# from os import mkdir
# from random import randint
#
# mkdir("/Users/cer6erus7/Desktop/Papochka")     # Включать только при создании папки
#
# for i in range(5):
#     with open(f"/Users/cer6erus7/Desktop/Papochka/{randint(0, 100)}.txt", 'w') as f:
#         f.write('lol')


# Problem 6
#
# from random import shuffle
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek",
#          "Dastan", "Maksat"]
#
# shuffle(names)
#
# chunked_list = list()
#
# for i in range(0, len(names), 4):
#     chunked_list.append(names[i:i+4])
#
# for i in chunked_list:
#     print(i)


# Problem 8
#
# from sys import getsizeof
#
# a = input('Print your first text - ')
# b = input('Print your second text - ')
#
# if getsizeof(a) > getsizeof(b):
#     print(f'First text is bigger then second! {getsizeof(a)} > {getsizeof(b)}')
# else:
#     print(f'Second text is bigger then first! {getsizeof(b)} < {getsizeof(a)}')


# Problem 9
#
# from random import randint
#
# number = int(input("Print the length of your password - "))
# password = []
#
# for i in range(number):
#     a = randint(0,9)
#     password.append(str(a))
# print(f'Your password - {"".join(password)}')


# Problem 10
#
# from random import choice
#
# print("If you want to see result type - /result")
#
# count_w = 0
# count_l = 0
# count_d = 0
#
# while True:
#     your_answer = input('\nPrint your answer(Scissor/Rock/Paper) - ').lower()           # Вводим данные
#
#     answers = ["scissor", "rock", "paper"]
#
#     if your_answer in answers:                                               # Проверяем результат
#         comp_answer = choice(["scissor", "rock", "paper"])
#         print(f"Computers answer                      - {comp_answer}\n")
#
#         if your_answer == 'paper' and comp_answer == 'scissor':
#             print('Computer won!')
#             count_l += 1
#         elif your_answer == 'scissor' and comp_answer == 'paper':
#             print('You won!')
#             count_w += 1
#         elif your_answer == 'scissor' and comp_answer == 'scissor':
#             print('Draw!')
#             count_d += 1
#
#         if your_answer == 'scissor' and comp_answer == 'rock':
#             print('Computer won!')
#             count_l += 1
#         elif your_answer == 'rock' and comp_answer == 'scissor':
#             print('You won!')
#             count_w += 1
#         elif your_answer == 'rock' and comp_answer == 'rock':
#             print('Draw!')
#             count_d += 1
#
#         if your_answer == 'rock' and comp_answer == 'paper':
#             print('Computer won!')
#             count_l += 1
#         elif your_answer == 'paper' and comp_answer == 'rock':
#             print('You won!')
#             count_w += 1
#         elif your_answer == 'paper' and comp_answer == 'paper':
#             print('Draw!')
#             count_d += 1
#
#     elif your_answer == '/result':                            # Конец программы
#         print(f"""
# Your win      - {count_w}
# Your lose     - {count_l}
# The Draw      - {count_d}""")
#         break
#
#     else:
#         print("Wtf, man? Type Scissor/Paper/Rock only!")         # Если данные неправильные


# Problem 11
#
# from random import randrange
#
# print(randrange(6, 12, 2))
# print(randrange(5, 100, 5))


# Problem 13
#
# import datetime
#
# current_date = datetime.datetime.now()
# print(current_date)
#
# date_1000 = current_date + datetime.timedelta(days=1000)
# print(date_1000)


# Problem 14
#
# NUMBERS = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
#
# a = 0
# b = 0
#
# for i in range(len(NUMBERS) // 2):
#     summ = NUMBERS[a] + NUMBERS[b+1]
#     print(summ)
#     a += 2


# Problem 15
#
# import datetime
# date = datetime.datetime.today()
# print(date.strftime('%H:%M'))


# Problem 16
#
# from time import sleep
#
# for i in range(10):
#     sleep(i)
#     print("I love you!")


# Probelem 17
#
# LIST1 = [1,3,5,7,9,11,13]
# LIST2 = [2,4,6,8,10,12,14]
#
# for i, x in zip(LIST1, LIST2):
#     print(i, x)