#2.Given a number x print out the following:

#If x is positive, print out x is positive.
#If x is negative, print out x is negative.
#If x is 0, print out x is 0.
#ans-
x = int(input("Enter a number: "))

if x > 0:
    print("x is positive.")
elif x < 0:
    print("x is negative.")
else:
    print("x is 0.")