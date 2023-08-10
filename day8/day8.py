# Problem 2
#
# with open('users.txt', 'w') as lol_kek:
#     login = input('Type your login - ')
#     password = input('Type your password - ')
#     lol_kek.write(login + ' ' + password)


# Problem 3
#
# with open('people.txt', 'w') as lol:
#     text = input("Print your text - ")
#     lol.write(text)
#
# with open('people.txt', "r") as file:
#     if 'w' in file.read():
#         print('Да, в тексте есть w')
#     else:
#         print('Нет, в тексте нет w')


# Problem 4
#
# with open('python.txt', 'w') as file:
#     file.write("""Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a resign philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.""")
#
# with open('python.txt', 'r') as file_1:
#     list_T = []
#
#     file_1 = file_1.read()
#     j = file_1.split(' ')
#
#     for i in j:
#         if 't' in i:
#             list_T.append(i)
#     print(list_T)


# Problem 5
#
# entrance = input('What do you want(login/sign)? - /').lower()
#
# while True:
#
#     if 'login' in entrance:
#
#         with open('database.txt', 'r') as f:
#             file = f.read()
#
#             users = file .split(',')
#             print(users)
#
#             login = input('\nWrite your login - ')
#             password = input('Write your password - ')
#
#             for i in users:
#                 if login == i.split(' ')[0] and password == i.split(' ')[1]:
#                     print('\nYour are on the site!')
#                     break
#                 else:
#                     print('\nYour password is incorrect! Try again!')
#                     break
#         break
#
#     elif "sign" in entrance:
#
#         with open('database.txt', 'a') as t:
#
#             login = input('\nWrite your login(without space) - ')
#
#             while True:
#                 password = input('Write your password - ')
#                 password_1 = input('Write your password again - ')
#                 if True:
#
#                     if password_1 == password:
#                         print('\nYou are successfully signed in!')
#                         t.write(f',{login} {password_1}')
#                         break
#                     else:
#                         print('Your passwords are incorrect! Try again!')
#         break
#     else:
#         print('Write only (login) or (sign)!')
#         break


# #
# with open('database.txt', 'r') as f:
#     file = f.read()
#
#     users = file.split(',')
#     print(users)
#
#
#     login = input('\nWrite your login - ')
#     password = input('Write your password - ')
#
#     for i in users:
#
#         if login in i.split(' ')[0]:
#             if password == i.split(' ')[1]:
#                 print('Your are on the site!')
#                 break
#             else:
#                 print('Password is incorrect!')
#
#                 print("\n Your login is incorrect! Sign in to create a new account!")
#                 with open('database.txt', 'a') as t:
#
#                     login_1 = input('Write your login - ')
#                     password_1 = input('Write your password - ')
#                     if True:
#                         password_2 = input('Write your password again - ')
#                         if password_2 == password_1:
#                             print('\nYou are successfully signed in!')
#                             t.write(f',{login_1} {password_1}')
#
#


# Problem 6
#
# login = input('Print your login - ')
# password = input('Print your password - ')
# image = input('Print direction of your photo - ')
#
# try:
#     with open(image, 'rb') as p:
#         p.read()
#         print('You were logged in!')
#
#         with open('database1.txt', 'w') as f:
#             f.write(f'{login}, {password}, {image}')
# except:
#     print('Wrong direction of your photo!')


# Problem 7
#
# image_1 = input("Type direction for your first photo - ")
# image_2 = input("Type direction for your second photo - ")
#
# count = 0
#
# try:
#     with open(image_1, 'rb') as p:
#         p.read()
# except:
#     count += 1
#
# try:
#     with open(image_2, 'rb') as i:
#         i.read()
#
# except:
#     count += 2
#
# if count == 1:
#     print("First file is incorrect")
# elif count == 2:
#     print("Second file is incorrect")
# elif count == 3:
#     print("Both of this files are incorrect")
# else:
#     with open(image_1 and image_2, 'ab') as la:
#         image_2 = image_1
#         print(f'image 2 = {image_2}')


# Problem 8
#
# with open('month.txt', 'r') as f:              # Открываем файл
#     lst = []
#
#     for i in f:                                             # Выбираем нужные нам месяцы и добавляем их в список
#         if 'May' in i.strip():
#             lst.append((int(i.split(' ')[-1])))
#         if 'July' in i.strip():
#             lst.append((int(i.split(' ')[-1])))
#         if 'September' in i.strip():
#             lst.append((int(i.split(' ')[-1])))
#         if 'November' in i.strip():
#             lst.append((int(i.split(' ')[-1])))
#
#     print(f"Среднее арифметическое за все эти месяци - {sum(lst) / 4}")   # Принтим результат


# Problem 9
#
# with open('first_spisochec', 'r') as f1:             # Открываем файл
#     file = f1.read()
#     lst = file.split(' ')
#
#     spisochec = []
#
#     for i in lst:
#         spisochec.append(int(i))
#
#     min_number = min(spisochec)                   # Берем самое большое число и самое маленькое
#     max_number = max(spisochec)
#
# with open('second_spisochec', 'w') as f2:             # Добавляем эти числа в другой список
#     f2.write(f'{str(min_number)} {str(max_number)}')


# Problem 10
#
# with open('test_file', 'w') as f:           # Выдает 3 ввода и в конце ввода принимает пустую строку
#     for i in range(3):
#         a = input('>> ')
#         f.write(a + '\n')