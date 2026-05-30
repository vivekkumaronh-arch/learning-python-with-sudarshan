dim=2

r1=[1,2]
r2=[3,4]
A=[]
A.append(r1)
A.append(r2)
print(A)

s1=[5,6]
s2=[7,8]
B=[]
B.append(s1)
B.append(s2)
print(B)

C=[[0,0],[0,0]]


for i in range(dim):
    for j in range(dim):
        
        C[0][0]=A[0][0]*B[0][0]+A[0][1]*B[1][0]
        C[0][1]=A[1][0]*B[0][0]+A[1][1]*B[1][0]
        C[1][0]=A[0][0]*B[0][1]+A[1][0]*B[1][1]
        C[1][1]=A[1][0]*B[0][1]+A[1][1]*B[1][1]
print(C)
