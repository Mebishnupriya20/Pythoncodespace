# 7.Given the variables x,y, and z print the following:

# if x and y are greater than 10, print step 1 is True
# if z or y is greater than x, print step 2 is True
# if step 2 is False, print step 2 is False
# ans-
x = 12
y = 15
z = 5

# Step 1
if x > 10 and y > 10:
    print("step 1 is True")

# Step 2
step2 = (z > x) or (y > x)

if step2:
    print("step 2 is True")
else:
    print("step 2 is False")