"""
Updated the loop range to iterate up to the second-to-last element to prevent the IndexError.
"""

def find_largest_diff(list_of_nums):
    largest_diff = 0
    # iterate up to the second-to-last element to prevent IndexError
    for i in range(len(list_of_nums) - 1):
        # calculate the absolute difference between consecutive numbers
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # the expected output should be 4.
    print(answer)
