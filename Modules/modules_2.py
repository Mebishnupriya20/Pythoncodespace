#Using randint create a random number x from 1 to 4. Then, print the number as a word. For example, if the number is 1, print one.
from random import randint
x = randint(1, 4)

if x == 1:
    print("one")
if x == 2:
    print("two")
if x == 3:
    print("three")
if x == 4:
    print("four")