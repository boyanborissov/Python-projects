# # s = [1,2,3,4,5]
# # print(s[1])
# # s[1]= 12
# # print(s)
#
# s =[]
# s.append(12)
# s.append(1)
# s.append(5)
# print(s)
# s[0] = 7
# print(s[0])
#
# # s=[1,2,3,4,5,6]
# # print(s[::-1]) извеждане елементите в обратен ред
# # print(s[:-1]) принтиране без последния елемент
# # print(s[1:]) принтиране без първия елемент
# # print(s[0:2]) първите два елемента
# # print(s[-1:]) последния елемент

#1
# number = int(input("Enter a numbers :"))
# list = []
# for i in str(number):
#     list.append(int(i))
# tup = tuple(list)
# print(tup)
# print(tup[::-1])
import random
#2
list= [1,2,3,4,5,6]
random.shuffle(list)
print(list)




