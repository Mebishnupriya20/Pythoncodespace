  # Given a list to_remove create a new set called numbers that contains the all numbers 1 through 10 that are not in to_remove

to_remove = [2, 5, 7]
numbers = {n for n in range(1, 11) if n not in to_remove}

print(numbers)