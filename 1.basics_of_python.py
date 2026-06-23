# First Python Program
print("Hello,World!")

'''print() is used to display output on screen.
"Hello World" is a string.}'''


# Comments                                      
'''
multi-line comment.

# Variables
name="VVK"
age=21
height=5.4


# Data Types
name="Hemant"      # string
age=32             # integer
price=59.80        # float 
is_student=True    # boolean 


# Type Checking
age = 18))   # type() tells the datatype of a variable.


# Taking Input
    # input() takes input from user.
name = input("Enter your name: ")    # Input is stored as string by default.
age  = int(input("Enter your age: "))

print(name)
print(age)


# Type conversion
age = input("Enter age: ")
age = int(age)
print(age)

int() convert to integer.
str() convert to string.
float() convert to float.
'''
 

# Operators
   # Arithmetic Operators
a=10
b=5
print(a+b)     # addition
print(a-b)     # subtraction
print(a*b)     # multiplication
print(a/b)     # division
print(a%b)     # remainder
print(a**b)    # power

   # Relational Operators (Output: True / False)
a=10
b=5
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

      # comparision of strings
print('apple'> 'banana')
print('abcdef'<'abcde')
print('az'>'ac')

   # Logical Operators
x=True 
y=False
print(x and y)
print(x or y)
print(not x)


# String slicing  {variable[start :end :step]}
name = "Python"
       #012345
    #-5-4-3-2-1
print(name[5])
print(name[2:5])
print(name[0:5:2])
print(name[::-1])

#A literal is the fixed value that can be stored in a variable.


# del function
a="sudarshan"
del a
print(a)


# String methods
x="i lOve mY iNdIa"
print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.swapcase())


y="python"
print(y.islower())
print(y.isupper())
print(y.istitle())


x=123
y='abc'
z='abc123'
a='abc123@#$'
print(x.isdigit())
print(y.isalpha())
print(z.isalnum())
print(a.isalnum())


x='----python----'
print(x.strip('-'))
print(x.lstrip('-'))
print(x.rstrip('-'))


x="Python"
print(x.startswith('p'))
print(x.endswith('n'))

x="I am 21 years old data scientist."
print(x.count('i'))
print(x.index('i'))
print(x.replace("y","T"))


