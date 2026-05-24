# normal loop
for i in range(10):
    print(i)         # default end is "\n",which means new line



# end function (without new line)
for i in range(10):
    print(i,end="love")


# sep function
d=15
m=3
y=2025
# print("Your anniversary is on",d,m,y,sep="-")
print("your anniversary is on",end=' ')
print(d,m,y,sep="-")


# f string method
num=int(input("Enter a number:"))
for i in range(1,11):
    # print(num,'X',i ,'=',num*i)
    print(f'{num} X {i} = {num*i}')

# .format method
num=int(input("Enter a number:"))
for i in range(1,11):
    # print(num,'X',i ,'=',num*i)
    print('{0} X {1}={2}'.format(num,i,num*i))

# old method or string modulo operator(%d,%f)
num=int(input("Enter a number:"))
for i in range(1,11):
    # print(num,'X',i ,'=',num*i)
    print('%d X %d = %d' %(num,i,num*i))


# Q. print value of pi using all 3 string methods
pi=22/7
print(f'Value of PI = {pi}')
print('Value of PI = {0}'.format(pi))
print('Value of PI = %f'%(pi))

# if we want fix decimal numbers(:.2f)
pi=22/7
print(f'Value of PI = {pi:.2f}')
print('Value of PI = {0:.2f}'.format(pi))
print('Value of PI = %.2f'%(pi))


# Formatted Printing in Python

print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))


# Explanation:
# 0  -> first value passed in format()
# 5  -> total width of output
# d  -> integer (decimal number)

# Output:
#     1
#    11
#   111
#  1111
# 11111

