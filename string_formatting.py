# python format() function
# "{}".format(value)

Bride="Deepika"
Groom="Ranveer"
Date="14 Nov 2018"

# Do remember the order
print("{} is married to {} on {}".format(Bride,Groom,Date))


# Another way to print, order doesn't matter here.
print("{Lady} is married to {Gentleman} on {Day}".format(Day = Date,Lady=Bride,Gentleman=Groom))


# format a string using f string
place="Classroom"
Tool="CCTV"
Topic="Notice"

print(f"{Topic}: This {place} is under {Tool} surveillance")


# format a string using %s,%d,%f

name="vivek"
age=21
marks=89.60

print("Hello everyone, My name is %s . I am %d years old. I got %f marks in 12th standard" %(name,age,marks))


