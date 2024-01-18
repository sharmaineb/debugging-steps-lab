"""
    Gather Information:
    - Expected vs. Actual Output:
      - Expected Output: The index of the element 7 in the given sorted array.
      - Actual Output: Error (RecursionError: maximum recursion depth exceeded in comparison).
    - Error Message:
      - `RecursionError: maximum recursion depth exceeded in comparison`
    - Line Number Causing the Error:
      - Line 34: `return binary_search(arr, element, low, mid)`
    - Deduction about the Cause of the Error:
      - The recursion depth is exceeding the limit, likely due to incorrect recursive calls.

    State Assumptions:
    - Assumptions:
      1. The binary search is performed on a sorted array.
      2. The recursive calls are meant to narrow down the search range (`low` and `high`).
    - Print Statements to Verify Assumptions:
      - Add a print statement before line 9: `print(f"Recursive call: low={low}, mid={mid}, high={high}")`
"""

def binary_search(arr, element, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element:
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid - 1)

    else:
        return binary_search(arr, element, mid + 1, high)

if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)

# Changes made:
# 1. Adjusted the recursive calls to narrow down the search range correctly.
