# if while doesn't exist.

print("When did India get its independence (year) ?")
year= int(input())

if year==1947:
    print("Hip Hip Hurray. You got that right!")
else:
    print("Come on don't you know even this?")
    print("That's ok, I will let you attempt this once more")
    print("when did India get its independence(year)?")
    year=int(input())
    if year==1947:
        print("That's all right.")
    else:
        print("Failed in your second attempt too? grrrr....")


# but while exists..
print("When did India get its independence (year)?")
year = int(input())

while(year != 1947):
    print("You need one more attempt..")
    year = int(input())
    
print("Wowwww. you got it right!")



