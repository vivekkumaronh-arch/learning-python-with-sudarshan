# break
email = input("Enter your email address:")
for c in email:
    if (c=="@"):
        break
    print(c,end=" ")
