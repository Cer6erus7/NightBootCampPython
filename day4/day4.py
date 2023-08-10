# Problem 1
#
# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#
#
# if lang1 in languages:
#     print('This languages is in list')
# else:
#     print('This languages is not in the list')


# Problem 2
#
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#
# for i in languages:
#     if i == 'php':
#         break
#     print(i)


# Problem 3
#
# a = 7
# for i in range(5):
#     a *= 7
#     print(a)


# Problem 4
#
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# a = 0
#
# for i in languages:
#     print(str(a) + ' ' + i)
#     a += 1


# Problem 5
#
# lst = []
# x = 0
#
# for i in range(1,20):
#     if i >= 10:
#         i = i - x
#         x += 2
#     lst.append(str(i))
# print(','.join(lst))

# Problem 6
#
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
#
# for i in range(len(names)):
#     if i % 2 == 0:
#         print(names[i])

# Problem 7
#
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
#
#
# for i in range(len(names)):
#     if i % 2 != 0:
#         print(names[i])


# Problem 8

# number = int(input('Type your number - '))
#
# if len(str(number)) == 3:
#  print('\nYour number have 3 digits!')
# else:
#  print('\nYour number have more or lower than 3 digits!')
#
# if number % 2 == 0:
#  print('This number is eval')
# else:
#  print('This number is odd')
#
# if number % 31 == 0:
#  print('This number can be divided by 31 and have no rest!')
# else:
#  print('This number cannot be divided by 31 without rest!')
#
# if number > 100 and number % 17 == 0 or number > 150 and number == 13**2:
#  print(f'This number - {number}')


# Problem 9
#
# list_0 = []
# list_1 = []
#
# for i in range(-100,101):
#
#     if i % 13 == 0:
#         a = i**2
#         list_0.append(a)
#
#     if i % 7 == 0:
#         if i % 2 != 0:
#             list_1.append(i)
#
# print(list_0)
# print(list_1)
# print('First task - ', len(list_0))
# print('Second task - ', len(list_1))
