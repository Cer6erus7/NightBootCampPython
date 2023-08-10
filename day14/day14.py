# Problem 1

# class Factory:
#
#     def engine(self):
#         return "Двигатель создан"
#
#     def bridge(self):
#         return "Ходовая часть создана"
#
#
# class Toyota(Factory):
#
#     def wheels(self):
#         return "Колёса готовы"
#
#     def windows(self):
#         return "Стёкла готовы"
#
#
# car = Toyota()
#
# lst = [car.wheels(), car.windows(), car.bridge(), car.engine()]
# print(lst)


# Problem 2

# class Zoo:
#     def __init__(self):
#         self.animal_1 = ""
#         self.animal_2 = ""
#         self.animal_3 = ""
#         self.animal_4 = []
#
# zoo = Zoo()
#
#
# zoo.animal_1 = "Тигр"
# zoo.animal_2 = "Бегемот"
# zoo.animal_3 = "Жираф"
#
# zoo.animal_1 = "Лев"
# zoo.animal_4 = [zoo.animal_2, zoo.animal_3]
#
# zoo.animal_3 = "Змея"
#
# print(zoo.animal_1, zoo.animal_2, zoo.animal_3, zoo.animal_4)