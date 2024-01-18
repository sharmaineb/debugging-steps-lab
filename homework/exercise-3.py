"""
    Gather Information:
    - Expected vs. Actual Output:
      - Expected Output: The sorted array using Insertion Sort.
      - Actual Output: Error (IndexError: list index out of range).
    - Error Message:
      - `IndexError: list index out of range`
    - Line Number Causing the Error:
      - Line 27: `while key < arr[j] :`
    - Deduction about the Cause of the Error:
      - The error occurs because the while loop condition (`key < arr[j]`) may lead to an attempt to access an index that is out of range.

    State Assumptions:
    - Assumptions:
      1. The loop iterates over the indices starting from 1 (`for i in range(1, len(arr))`).
      2. The while loop is meant to shift elements to the right until the correct position for `key` is found.
    - Print Statements to Verify Assumptions:
      - Add a print statement before line 9: `print(f"Processing index {i}, key: {key}")`
      - Add a print statement before line 10: `print(f"Comparison: {key} < {arr[j]}")`
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

# Changes made:
# 1. Added the condition `j >= 0` to the while loop to prevent accessing an index that is out of range.
