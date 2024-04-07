"""

Given an array with positive numbers and a target number, 
find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.

"""

from collections import deque

# we will use a sliding window to get the subarrays that have product < k


def find_subarrays(arr, target):
    # initialize variables
    res = []  # list containing all the subarrays
    product = 1
    l = 0  # left pointer

    # traverse through the array with right pointer
    for r in range(len(arr)):
        product *= arr[r]  # multiplying the number at the right pointer

        # the product might get bigger than target so we try to shrink the window until it gets smaller
        while product >= target and l < len(arr):
            product /= arr[l]
            l += 1

        # get all the subarrays ending at index r
        temp_list = deque()
        for i in range(r, l - 1, -1):
            temp_list.appendleft(arr[i])
            res.append(list(temp_list))

    return res


# test the function
if __name__ == "__main__":
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))
