"""
  Gather Information
    - Expected Output (for the first call): False
    - Actual Output (for the first call): True
    - Expected Output (for the second call): True
    - Actual Output (for the second call): False
    - No error message, but the actual output does not match the expected output.
  - Line Number Causing the Error:
    - Line 29: `return False`
  - Deduction about the Cause of the Error:
    - The function returns False too early within the loop, causing incorrect results.

  State Assumptions
  - Assumptions:
    1. The loop iterates over the indices up to the third-to-last element (`len(list_of_nums) - 2`).
    2. The function returns True if three consecutive numbers in the list increase by 1.
  - Print Statements to Verify Assumptions:
    - Add a print statement before line 10: `print(f"Processing index {i}, list values: {list_of_nums[i]}, {list_of_nums[i+1]}, {list_of_nums[i+2]}")`
    - Add a print statement before line 11: `print(f"Comparison: {list_of_nums[i+1]} == {list_of_nums[i] + 1} and {list_of_nums[i+2]} == {list_of_nums[i] + 2}")`

"""

def contains_3_consecutive(list_of_nums):
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1)  # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2)  # should print True

# Changes made:
# Moved the `return False` statement outside of the loop to ensure it only returns False after checking all possible sets of three consecutive numbers.

