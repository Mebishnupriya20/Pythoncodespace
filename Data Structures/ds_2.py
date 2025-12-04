  # Given a sequence numbers print the median of the sequence. 
# Note: your solution should work if the sequence is a list or tuple.


def find_median(numbers):
    nums = sorted(numbers)      # Works for both list and tuple
    n = len(nums)

    # If count is odd
    if n % 2 == 1:
        return nums[n // 2]
    # If count is even
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2


# Example test cases
print(find_median([3, 1, 4, 2, 5]))     # List
#  print(find_median((10, 2, 8, 4)))       # Tuple