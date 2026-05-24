import math as m
print(m.log(10))
print(m.sin(90))
print(m.sqrt(9))
print(m.factorial(5))
print(m.pow(10,3))

import random
print(random.random())

# Let us simulate a coin toss.
import random
a=random.random()

if (a<.5):
    print("Heads")
else:
    print("Tails")

# Let us simulate a dice(six faced).
import random
print(random.randrange(1,7))

# Let us simulate the sum of two dices.
import random
dice1=random.randrange(1,7)
dice2=random.randrange(1,7)
total=dice1 + dice2
print("your pair of dice is",total)
