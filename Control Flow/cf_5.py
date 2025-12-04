#5.Given a number x, use continue to print out even numbers from 0 to x. Use break Stop if you reach a number greater than 20.
#ans-
x = int(input("Enter a number: "))

for i in range(x + 1):
    if i > 20:
        break
    if i % 2 != 0:
        continue
    print(i)