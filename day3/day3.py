# Problem 1
#
# a = 2**3
# b = 3**2
# if a > b:
#     print('a > b')
# else:
#     print('a < b')


# Problem 2
#
# a = int(input('Print 1 - '))
# b = int(input('Print 2 - '))
# c = int(input('Print 3 - '))
#
# if c < a > b:
#     print(f'Biggest number - {a}')
# elif c < b > a:
#     print(f'Biggest number - {b}')
# else:
#     print(f'Biggest number - {c}')
#
# if c > a < b:
#     print(f"Lowest number - {a}")
# elif a > b < c:
#     print(f"Lowest number - {b}")
# else:
#     print(f"Lowest number - {c}")


# Problem 3
#
# a = 17391 % 17
# b = 546 % 17
# c = 934 % 17
#
# print(a,b,c)
#
# if b > a < c:
#     print(f'Самая маленькая остача это {a} от числа 17391')
# elif a > b < c:
#     print(f'Самая маленькая остача это {b} от числа 546')
# else:
#     print(f'Самая маленькая остача это {c} от числа 934')


# Problem 4
#
# x = 13
# print(x)
# print(f'{x} **= 2')
#
# x **= 2
#
# if x > 172:
#     print(f"{x} > 172")
# else:
#     print(f'{x} **= 2')
#     x **= 2
#
# if x > 172:
#     print(f"{x} > 172")
# else:
#     x **= 2
#     print(f'{x} **= 2')


# Problem 5
#
# x = int(input('Type your number - '))
#
# if x % 2 == 0:
#     print('Your number is eval!')
# else:
#     print('Your number is odd')
#
# if x % 3 == 0:
#     print('Your number divided by 3 and rest is 0!')
# else:
#     print('Your number cannot divide by 3 without the rest!')
#
# if x ** 2 > 1000:
#     print('Your number is bigger than 1000!')
# else:
#     print('Your number is lower than 1000!')


# Problem 6
#
# x = int(input("Write your number - "))
#
# if 0 <= x <= 21 or 57 <= x <= 100:
#     print(f'You can write this nimber - {x}')
# else:
#     print(f'You cannot write this number - {x}')


#  Problem 7
#
# if True:
#     print("lol")


# Problem 8
#
# x = 5
# lol = "Lol kek"
#
# if x < 10:
#     if x > 3:
#         if x == 5:
#             print(lol)


# Problem 9
#
# a = 10//5
# b = 10/5
#
# if a == b:
#     print(f"10 // 5 = {a}")
#     print(f"10 / 5 = {b}")
# else:
#     print("There are not equal!")


# Problem 10
#
# x = int(input("Print your number - "))
#
# if x < 0:
#     print(f"Your number: {x}")
# else:
#     print("You can write only negative numbers!")


# Problem 11
#
# a = 10
# b = 5
#
# if a > 0 and b > 0:
#     print('"a" and "b" are positive numbers!')
# else:
#     print("One or two of your numbers are negative!")


# Problem 12
#
# a = 10
# b = 5
#
# if a > b:
#     a += 2
#     print(f"a + 2 = {a}")
# else:
#     b += 2
#     print(f"b + 2 = {b}")