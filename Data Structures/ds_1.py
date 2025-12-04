# Create a list named numbers with the numbers 4, 5, and 6
# Given a list named hidden, add 5, remove 2, and then sort. numbers = [4, 5, 6]
numbers = [4, 5, 6]
hidden = [1, 2, 3, 7, 8]
hidden.append(5)
hidden.remove(2)
hidden.sort()

print(f"Numbers list: {numbers}")
print(f"Hidden list after operations: {hidden}")