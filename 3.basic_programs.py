print("Hello,type in your name:")
n=input()
print("Which place are you in?")
p=input()
print("Which is your favourite weather?")
w=input()
print("Hello",n,",I hope you are enjoying",w,"weather in",p)



alpha="abcdefghijklmnopqrstuvwxyz"
s="india"
# I expect to output joejb
t=''
i=0
t=t+(alpha[(alpha.index(s[i])+1)%26])
t=t+(alpha[(alpha.index(s[i+1])+1)%26])
t=t+(alpha[(alpha.index(s[i+2])+1)%26])
t=t+(alpha[(alpha.index(s[i+3])+1)%26])
t=t+(alpha[(alpha.index(s[i+4])+1)%26])
print(t)