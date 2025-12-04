#6.Given the variables x,y, and z, print the sum of the values that are not None.
#ans-
x = 5
y = None
z = 10

values = [x, y, z]

total = sum(v for v in values if v is not None)

print("Sum:", total)