'''1'''

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def __eq__(self, other):
#         return self.radius == other.radius

#     def __lt__(self, other):
#         return self.radius < other.radius

#     def __gt__(self, other):
#         return self.radius > other.radius

#     def __le__(self, other):
#         return self.radius <= other.radius

#     def __ge__(self, other):
#         return self.radius >= other.radius

#     def __add__(self, other):
#         return Circle(self.radius + other.radius)

#     def __iadd__(self, other):
#         self.radius += other.radius
#         return self

#     def __sub__(self, other):
#         return Circle(self.radius - other.radius)

#     def __isub__(self, other):
#         self.radius -= other.radius
#         return self

# circle1 = Circle(5)
# circle2 = Circle(5)
# circle3 = Circle(7)



# circle1 += circle3
# print(circle1.radius)

# circle2 -= circle3
# print(circle2.radius)


'''3'''
# class Airplane:
#     def __init__(self, model, max_passengers, current_passengers):
#         self.model = model
#         self.max_passengers = max_passengers
#         self.current_passengers = current_passengers

#     def __eq__(self, other):
#         return self.model == other.model

#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers

#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers

#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers

#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers

#     def __add__(self, passengers):
#         if self.current_passengers + passengers <= self.max_passengers:
#             self.current_passengers += passengers
#         else:
#             print("Cannot add more passengers, exceeding max capacity!")
#         return self

#     def __iadd__(self, passengers):
#         return self.__add__(passengers)

#     def __sub__(self, passengers):
#         if self.current_passengers - passengers >= 0:
#             self.current_passengers -= passengers
#         else:
#             print("Cannot remove more passengers than current on board!")
#         return self

#     def __isub__(self, passengers):
#         return self.__sub__(passengers)

# plane1 = Airplane("Boeing 747", 500, 200)
# plane2 = Airplane("Airbus A380", 600, 300)
# plane3 = Airplane("Boeing 777", 400, 250)


# plane1 += 100
# print(plane1.current_passengers)
# plane2 -= 400
# print(plane2.current_passengers)
# print(plane2.max_passengers)


'''4'''

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

flat1 = Flat(80, 100000)
flat2 = Flat(70, 90000)
flat3 = Flat(80, 110000)

print(flat2 < flat1)
print(flat2 > flat3)
print(flat3 > flat1)
print(flat3 > flat2)
print(flat1 > flat2)
print(flat1 > flat3)