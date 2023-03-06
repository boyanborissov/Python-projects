#1
# printer = int(input("Enter a number: "));
# printer2 = int(input("Enter a second number: "))
#
# def square():
#     area = printer*printer
#     print(area)
# square()
#
# def rectangle():
#     area2=printer*printer2
#     print(area2)
# rectangle()
#
# def rectangleTriangle():
#     area3=(printer*printer2)/2
#     print(area3)
# rectangleTriangle()

#2
#
# def isPalindrome(s):
#     return s == s[::-1]
#
#
# # Driver code
# s = input("Enter a number: ")
# ans = isPalindrome(s)
#
# if ans:
#     print("1")
# else:
#     print("0")

#3
print = int(input("Enter a number: "))
operation = ("Enter a operation: ")
print2 = int(input("Enter a second number: "))


def sum():
    a =1
    summary= print + print2;
    print(summary)
sum()

def sub():
a=2
    substract= print - print2;
    print(substract)
sub()


def multiply():
    a = 3
    multiply= print * print2;
    print(multiply)
multiply()

def divide():
    a = 4
    divide= print / print2;
    print(divide)
divide()

if(a == 1):
    sum()
elif (a == 2):
    sub()
elif (a == 3):
    multiply()
elif (a == 4):
    divide()
