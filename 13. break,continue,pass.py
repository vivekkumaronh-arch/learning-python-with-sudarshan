'''In Python, break, continue, and pass are control flow statements used to alter 
the execution behavior of loops and block structures.

pass = "Ignore and move normally"
continue = "Skip this iteration"
break = "Stop the loop"'''



# break
email = input("Enter your email address:")
for c in email:
    if (c=="@"):
        break
    print(c,end="")


# Continue
email="24f2002200@ds.study.iitm.ac.in"
for c in email:
    if (c=="@"):
        print('')   # it actually does nothing but creates an extra line to separate from '@' while ignoring it.
        continue
    print(c,end='')


# pass
for i in range(11):
    if i%3==0:
        print(i)
    else:
        pass