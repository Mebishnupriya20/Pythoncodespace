
# Get the absolute value of each number in secret
# For each index add the number in key to the result of step 1
# Reverse the order of the numbers in the result of step 2
# Use integer division to divide each number in the result of step 3 by 5
# Add the index of each number in step 4 to its value
# Convert each value to a character
# use ''.join(list) to convert a list of characters to a string
secret = [-12, 8, -25, 17]
key = [3, 6, 2, 4]

# 1. Get absolute values
step1 = [abs(n) for n in secret]

# 2. Add matching index value from key
step2 = [step1[i] + key[i] for i in range(len(secret))]

# 3. Reverse the list
step3 = step2[::-1]

# 4. Integer divide each value by 5
step4 = [n // 5 for n in step3]

# 5. Add index to each number
step5 = [step4[i] + i for i in range(len(step4))]

# 6. Convert each value to a character
chars = [chr(n) for n in step5]

# 7. Join into a string
result = ''.join(chars)
