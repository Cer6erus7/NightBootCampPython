# Problem 1
#
# class Problems:
#     def __init__(self, data):
#         self.marker = data["MARKERS"]
#
#     def hotels_name(self):
#         return [i["NAME"] for i in self.marker]
#
#     def tuplik(self):
#         names = []
#         location = []
#
#         for i in self.marker:
#             if "NAME" in i:
#                 names.append(i["NAME"])
#             if "LOCATION" in i:
#                 location.append(i["LOCATION"])
#
#         tuplik1 = tuple(names)
#         tuplik2 = tuple(location)
#         return {"Names": tuplik1, "Locations": tuplik2}
#
#
#     def add_id(self):
#         for i in self.marker:
#             i["Status_ID"] = 1
#         return self.marker
#
# DATA = {
#
# "MARKERS": [
#
# {
#
# "NAME": "RIXOS THE PALM DUBAI",
#
# "POSITION": [25.1212, 55.1535],
#
# },
#
# {
#
# "NAME": "SHANGRI-LA HOTEL",
#
# "LOCATION": [25.2084, 55.2719]
#
# },
#
# {
#
# "NAME": "GRAND HYATT",
#
# "LOCATION": [25.2285, 55.3273]
#
# }
#
# ]
#
# }
#
# a = Problems(DATA)
# print(a.hotels_name())
# print(a.tuplik())
# print(a.add_id())


# Problem 2

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
