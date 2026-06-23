for i in range(10):
   print(i)


# code to add first 11 integers
# 0+1+2+3+4+5+6+7+8+9 = 45
'''
ans=0+1+2+3+4+5+6+7+8+9
print(ans)
'''

ans=0
for i in range(0,10):
    ans=ans+i

print("The answer is",ans)



# write a code to add first n integers

print("Enter a number:")
n=int(input())

ans=0
for i in range(n):
    ans=ans+i

print("The sum of first n integers are ",ans)


# print string using for loop
for i in range(1,11):
 print(i,"Hello ji")



# print a table of 15 
for i in range(1,11):
   # print("15 X",i,"=",15*i)
   print(f'15 X {i} = {15*i}')



# finding odd no. between given range
for i in range(1,21):
   if (i%2 !=0):
      print(i)
# OR
for i in range(1,21,2):
   print(i)

# finding even no. between given range
for i in range(1,21):
   if (i%2 ==0):
      print(i)



# reverse printing numbers
for i in range(10,0,-1):
   print(i)


# for loop without range
Country="Japan"
for letter in Country:
   print(letter)
   


# find the factorial of a number using for loop
num=int(input("Enter a number: "))
fact=1
if num<0:
   print("Not defined")
else:
   for i in range(num,1,-1):
      fact=fact*i
   print("Factorial of",num,"is",fact)




# WAP to print Fibonacci Series
for i in range(10):
   a=0
   b=1
   a+=b
   print(a)
   

for num in range(100)
   for i in range(100):
      if i % num:
         print(i)




   
