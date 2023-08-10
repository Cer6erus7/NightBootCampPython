# Problem 1
#
# print(17925 <= (34**2))
# print(17925 <= (26*3))
# print(17925 <= (17*33))
# print(17925 <= (4394*4))


# Problem 2
#
# a = 15
# b = 10
# c = 20
#
# print(c>a>b)
# print(7/3*4.8)
# print(1+1==3-1)
# print(1+1==2-1)


# Problem 3
#
# a = 12+43
# b = a * 23
# c = b**2
# d = c - 193432
# print(d)


# Problem 4
#
# print((17*3)<(12*5))
# print((12**3)>(13*7))
# print((4**5)==(512+512))


# Problem 5
#
# print(-21//10)
#
# Потому что это деление с округлением в меньшую, а -3 меньше -2.1


# Problem 6 ?
#
# a = 23
# b = 77
# print((a/b)*100)


# Problem 7
#
# my_birthday = 2001
# year = 2020
# print(year - my_birthday + 2)
# print(year - my_birthday - 2)


# Problem 8
#
# a = 25
# b = 75
# c = 10
# d = 95
# print((a+b+c+d)/4)


# Problem 9
#
# a = 2.3
# b = 2.3
# c = 2.3
# print((a+b)*c)


# Problem 10
#
# a = 12
# b = 7
# c = 14.7
# d = 9
# e = 34


# Problem 11
#
# a = 12
# b = 7
# c = 14.7
# d = 9
# e = 39
# print((a-e**(b/d))%c)

from random import choice
import json


with open("lol.json", "r") as f:
    data = json.load(f)
    print(choice(data['sport']))