 # Given a list numbers create a dictionary called counts that contains the number of times each number appears in the list.

numbers = [1, 2, 2, 3, 3, 3, 5, 5]

# Create the dictionary of counts
counts = {}

for n in numbers:
    counts[n] = counts.get(n, 0) + 1

print(counts)