#if condition
# Let us cosider the movie "3 Idiots".This is a 13+ movie.

print("Please, Enter your birth year:")
birth_year=int(input())
current_year=2026
age=current_year - birth_year

if (age<13):
    print("You are under age, you cannot watch this movie.")
else:
    print("You are old enough to watch '3 Idiots'.")

print("Have a nice time.")



# Q. Write a code to distinguish entered no. is even or odd.
num=int(input("Enter a number:"))
if (num%2==0):
    print(num, "is even.")
else:
    print(num,"is odd.")


