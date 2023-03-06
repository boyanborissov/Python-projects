#
# #2
# import re
# str = 'Data 34-5643 12-06-2020 , XYZ 65 2345 11-07-2021'
# match = re.findall('[\d]{1,2}-[\d]{1,2}-[\d]{4}',str)
# for s in match:
#     print(s)
#1
# import re
# text = "Hello, my name is Ivan Petrov. You can contact me at ivan.petrov@test.com. Tomorrow Maria Ivanova will call you with details about the meeting"
# match = re.findall("[^.] ([A-Z][a-z]+ [A-Z][a-z]+)",text)
# for s in match:
#     print(s)
def even_positive():
    number = int(input())
    if number >= 0:
        print("Number is positive", end =' ')
    else:
        print("Number is negative", end=' ')
    if number % 2 == 0:
        print("and it is even.")
    else:
        print("and it is odd.")