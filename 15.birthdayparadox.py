# # creating lists from random import

# import random
# l=[]
# for i in range(10):
#     l.append(random.random())
# print(l)



# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(1,10))
# print(l)


'''Birthday paradox is a probability concept which states that in a group of only 23 people, 
there is about a 50% chance that two people will have the same birthday.
10 people → ~12% chance of a shared birthday
23 people → ~50% chance
30 people → ~70% chance
50 people → ~97% chance'''

# import random
# l=[]   # create an empty list
# for i in range(40):
#     l.append(random.randint(1,365))

# # print(l)

# l.sort()     # sort() is used to arranged numbers in increasing order.
# print(l)

# # here we need to check manually , which one is repeating, so write a code to tell where it repeats.




import random
l=[]
for i in range(50):
    l.append(random.randint(1,365))
l.sort()
print(l)

i=0
flag=0    # denotes that there is no repetition
while (i<len(l)-1):
    if (l[i]==l[i+1]):
        print(l[i],"repeats")
        flag=1
        
    i=i+1

if flag==0:
    print("There is no repetition.")

