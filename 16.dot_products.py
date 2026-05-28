a=[2,5,9,7]
b=[9,5,4,3]
# dot_product=(2*9)+(5*5)+(9*4)+(7*3)
# print(dot_product)

sum=0
for i in range(len(a)):
    sum=sum+(a[i]*b[i])
    i+=1
print("Dot product of a and b:",sum)

