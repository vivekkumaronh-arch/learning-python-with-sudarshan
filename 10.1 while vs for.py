# # Problem 1. Find the factorial of a given number
# # Using while loop:
# num = int(input("Enter a number:"))
# original=num
# fact=1
# if (num<0):
#     print("Not Defined")
# else:
#     while(num>0):
#         fact=fact*num
#         num-=1
#     print(f'Factorial of {original} is {fact}')


# # Using For loop:
# num=int(input("Enter a number:"))
# fact=1
# if num<0:
#     print("Not Defined")
# else:
#     for i in range(num,1,-1):
#         fact=fact*i
#     print(f'Factorial of {num} is {fact}')



# # Problem 2. find the number of digits in the given number

# #We can't solve it using for loop, because we don't know the no. of iteration, it can be unlimited.

# num=abs(int(input("Enter a number:")))
# digits=0
# while num>0:
#     num=num//10
#     digits+=1
# print(f'number of digits in given number is {digits}.')

# # Actually we can solve it using for loop but it is not supposed to be ideal use
# num=abs(int(input("Enter a number:")))
# strNum=str(num)
# digits=0
# for i in strNum:
#     digits+=1
# print("No. of digits in given no. is",digits)



# # Problem 3. Reverse the digits in the given number
# #using while loop                                        (********not understood properly************)
# num = int(input("Enter a number:"))
# absNum = abs(num)

# rev = absNum % 10
# absNum = absNum // 10

# while(absNum > 0):
#     r = absNum % 10
#     absNum = absNum // 10
#     rev = rev * 10 + r

# if(num > 0):
#     print(rev)
# else:
#     print(rev - 2 * rev)


# # #using for loop
# num=int(input("Enter a number:"))
# absStrNum=str(abs(num))
# rev=''
# for i in absStrNum:
#     rev=i+rev
# if num>0:
#     print(rev)
# else:
#     print("-",rev)



# # Problem 4: Find whether the entered no. is palindrome or not
# #using while loop                               (********not understood properly************)
# num = int(input("Enter a number:"))      
# absNum = abs(num)

# rev = absNum % 10
# absNum = absNum // 10

# while(absNum > 0):
#     r = absNum % 10
#     absNum = absNum // 10
#     rev = rev * 10 + r

# if(num < 0):
#     rev=rev-2*rev
# if (rev==num):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")



# # using for loop
# num=int(input("Enter a number:"))
# absStrNum=str(abs(num))
# rev=''
# for i in absStrNum:
#     rev=i+rev
# if num<0:
#     rev="-" + rev
# if num==int(rev):
#     print("Palindrome")
# else:
#     print("Not Palindrome")













