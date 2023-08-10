# Problem 1
#
# list_1 = ['name', 'age', '1', '19']
#
#
# def reverse_list():
#     my_list1 = list_1[0:len(list_1)//2]
#     my_list2 = list_1[len(list_1)//2:len(list_1)]
#     total = my_list1[::-1] + my_list2[::-1]
#     print(total)
#
# reverse_list()


# Problem 2
#
# lst = []
#
# def fabinachi():
#     x = 1
#     z = 1
#     for i in range(10):
#         lst.append(x)
#         y = x + z
#         x = z
#         z = y
#     print(lst)
#
# fabinachi()


# Problem 3
#
# def ans():
#     a = float(input("Print first number - "))
#     b = float(input("Print second number - "))
#
#     def subs():
#         y = a - b
#         print(f"(-) Answer is - {y}")
#
#     def sums():
#         c = a + b
#         print(f"(+) Answer is - {c}")
#
#     sums()
#     subs()
# ans()


# Problem 4
#
# def file():
#     file_name = input('Print name of file - ')
#
#     with open(f"{file_name}.txt", 'w') as f:
#         f.write('')
#
# fun = file()
#
# print(fun)


# Problem 5
#
# from random import choice
#
# def gen_number():
#     list = [1,4,5,7,9,0]
#     list_1 = []
#
#     for i in range(0,6):
#         digits = choice(list)
#         list_1.append(str(digits))
#
#     print(f'0444 {("".join(list_1))}')
#
# gen_number()