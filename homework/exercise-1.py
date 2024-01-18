"""
  Gather Information:
  - Expected vs. Actual Output:
    - Expected Output: The largest difference between consecutive numbers in the given list.
    - Actual Output: Error (IndexError: list index out of range).
  - Error Message:
    - `IndexError: list index out of range`
  - Line Number Causing the Error:
    - Line 26: `diff = abs(list_of_nums[i] - list_of_nums[i+1])`
  - Deduction about the Cause of the Error:
    - The error occurs because the loop tries to access an index that is out of range when `i` is equal to the last index of the list.

  State Assumptions:
  - Assumptions:
    1. The loop runs through each element of the list using the index `i`.
    2. The difference between consecutive numbers is calculated using `list_of_nums[i]` and `list_of_nums[i+1]`.
  - Print Statements to Verify Assumptions:
    - Add a print statement before line 8: `print(f"Processing index {i}, list value: {list_of_nums[i]}")`
    - Add a print statement before line 9: `print(f"Calculating difference: {list_of_nums[i]} - {list_of_nums[i+1]}")`
"""

def find_largest_diff(list_of_nums):
    largest_diff = 0
    for i in range(len(list_of_nums) - 1):
        # checks the difference between consecutive numbers
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # the expected output should be 4.
    print(answer)
