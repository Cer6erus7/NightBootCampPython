# Problem 2
#
# numbers = set()
# for i in range(5):
#     x = input("Input your number - ")
#     numbers.add(x)
# print(min(numbers))


# Problem 3
#
# while True:
#    try:
#        question = input('Type your code: ')
#        if True:
#            question = eval(question)
#            print(question)
#            break
#    except:
#        print('ERROR! Type your code again!')


# Problem 4
#
# while True:
#    try:
#        credit = float(input("Write your credit: "))
#        percentage = 3.47
#        if credit >= 50000:
#            Formula = credit * (percentage / 100) + credit
#            print("Your credit is ", round(Formula, 2))
#        else:
#            print("You cannot borrow lower than 50000!")
#    except:
#        print("Write your credit properly!")

# Problem 1
#
# value = '5'
# print(value + 1)
#
# print(NameError)
#
# lists = [1]
# print(lists[2])


# Problem 3
#
# lst = []
#
# for i in range(10):
#    lst.append(i)
#    a = list(reversed(lst))
#    sls_obj = slice(0,8)
#    print(a[sls_obj])


# Problem 4
#
# a = (0)
# b = (1)
# numbers = []
# while b > a:
#     numbers.append(b)
#     b += 1
#     print(numbers)


# Problem 1
#
# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
# try:
#     for x in dict_.keys():
#         x + 'abc'
#         print(x)
# except TypeError:
#     print(f"В словаре один из ключей записан как 'int' - {x}")