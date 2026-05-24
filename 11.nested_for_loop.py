# find the no. of ways in which two brother can wear 7 different colours ?
s="VIBGYOR"
t="VIBGYOR"

count=0
for i in range(7):
    for j in range(7):
     print(i,j,s[i],t[j])
     count+=1       # same as count=count+1
     
print("The total ways in which two brother can wear 7 different colours:",count)