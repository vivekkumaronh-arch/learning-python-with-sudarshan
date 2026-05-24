# Let us find the factorial of a number using while loop
n=int(input("Enter a number: "))

i=1
answer=1
while (i<=n):
    answer = answer*i
    i=i+1
print("factorial of",n,"is",answer)


# 2nd way to find factorial 

num=int(input('Enter a number: '))
original=num
fact=1
if (num<0):
    print("Not defined")
else:
    while (num>0):
        fact=fact*num
        num-=1
    print("factorial of",original,"is",fact)