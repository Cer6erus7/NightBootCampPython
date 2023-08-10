# Problem 0
#
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# dates_of_birth.discard(6)
# print(dates_of_birth)


# Problem 1
#
# a = {1,2}
# b = {3,4}
# c = {5,6}
#
# a.update(b,c)
# print(a)


# Problem 2
#
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
#
# print(farm_2.difference(farm_1))


# Problem 3
#
# set_1 = {2,'d',3,True,'bull'}
# set_1.add('lol')
# set_1.pop()
#
# print(set_1)


# Problem 10
#
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
#
# menu['Drinks'] = 'Coca-Cola', 'Sprite', 'Fanta'
# print(menu)


# Problem 20
#
# method_set = {'.add("*")', '.remove("*")', '.clear()', '.update("*")', '.difference("*")', '.discard("*")', '.intersection("*")', '.intersection_update(*)', '.pop()'}
# method_dict = {'.clear()','.keys()','.items()','.get("*")','.values()','.update("*")'}
#
# method_set.intersection_update(method_dict)
# print(method_set)


# Problem 31
#
# log = {}
#
# for i in range(3):
#     name = input('Type your name: ')
#     password = input('Type your password - ')
#     log[name] = password
#
# print(log)


# Problem 27
#
# dict = {'Matvey': 'Programmer', 'Ernest': 'Chort', 'Ignat': 'Employee', 'Nastya': 'Operator', 'Ilona': 'Student'}
#
# for i in dict.keys():
#     print(f'Здравствуйте {i} Прекрасная профессия {dict[i]}')


# Problem 22
#
# set_1 = set()
# for i in range(10):
#     x = input("Type your number = ")
#     set_1.add(x)
# set_1  = tuple(set_1)
# print(set_1)


# Problem 99
#
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_barmak'] = 130
#
# if menu['lagman'] < 135:
#     menu['lagman'] = 135
#
# menu.pop('borsh')
# print(menu)


# Problem 11
#
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# south_american_countries = set(south_american_countries)
# print(list(south_american_countries))


# Problem 101
#
# suitcase = []
# for i in range(5):
#     things = input('Type your thing - ')
#     suitcase.append(things)
# print(suitcase)
#
# suitcase.pop(-1)
# print(suitcase)


# Problem 001
#
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
#
# farm_1.update(farm_2)
# print(farm_1)
#
# if True:
#     print(farm_1.difference(farm_2))