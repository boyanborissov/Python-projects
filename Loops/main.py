#for number in range (1,11):
    #print(number)

#for number in range(20,10,-2):
    #print(number)

#word = 'Python'
#for letter in word:
    #print(letter)

# for letter in range(ord('a'), ord('z') + 1):
#     print(chr(letter))

# number = 1
# while number <= 11:
#     print(number)
#     number+=1

# for number in range(1,20):
#     if number == 5:
#         continue
#     if number == 15:
#         break
#     print(number)

# number = int(input("Enter number: "))
# sum = 0;
# while True:
#     sum +=number%10
#     number = number//10
#     if not number:
#         break
# print(sum)

#1
# numbers = [1,2,3,4,5,6,7,8,9]
# max_number = max(numbers)
# print(max_number)

#2
# sum=0
# for numbers in range(1,11):
#     sum+=numbers
# print(sum)

#3
# n =5
# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     print()

#4
n = int(input("Enter number: "))
for i in range(2,n):
    if n % i  == 0 and n//1:
        print("Не е просто")
        break
else:
    print("Просто е")
