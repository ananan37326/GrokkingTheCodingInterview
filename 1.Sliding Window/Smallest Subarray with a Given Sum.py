'''
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

'''
import math # we will use math.inf  

def smallest_subarray_with_given_sum(s,arr):
    # declaring variables
    l = 0 # left pointer starting ar index 0
    sum = 0 # sum of the window
    min_length = math.inf # initializing the mean length as inf

    # looping through the array with right pointer
    for r in range(len(arr)):
        sum += arr[r]

        while sum >= s:
            min_length = min(min_length, r-l+1) # determining the minimum length of the window

            sum -= arr[l]
            l += 1

    return 0 if min_length == math.inf else min_length 


# test the code
if __name__=="__main__":
    arr = [2, 1, 5, 2, 3, 2]
    s = 7
    print(smallest_subarray_with_given_sum(s,arr))

