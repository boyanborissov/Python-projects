#1
# def sumRange(start, end):
#     if(start > end):
#       temp = start
#       start = end
#       end = temp
#
#     sum = 0
#     for i in range(start, end):
#        sum += i
#
#     print(sum)
#
# sumRange(1,5)
# sumRange(11,1)

#2
# class Limonada:
#     def __init__(self, supplement):
#         self.supplement = supplement
#
#     def show_my_drink(self):
#         if (self.supplement == ""):
#             print("Обикновена сода")
#         else:
#             print("Limonade and " + self.supplement)
#
# limonade = Limonada("sugar")
# limonade.show_my_drink()
# limonade = Limonada("")
# limonade.show_my_drink()

#3
# class Ivan:
#     __slots__ = ['name', 'age']
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_name(self):
#         if(self.name != "Ivan"):
#             print("I am not " + self.name + ", I am Ivan")
#         else:
#             print("Nice")
#
# name = Ivan("Vesko",12)
# name.print_name()
# name = Ivan("Ivan",12)
# name.print_name()

#4
def read_last(lines,file)
