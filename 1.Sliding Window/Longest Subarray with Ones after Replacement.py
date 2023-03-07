'''
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''

# same as longest substring with same letters after replacement, except we have only 1s and 0s
def length_of_longest_substring(arr,k):
    #declaring variables
    l = 0 # left pointer
    max_ones = 0 # number of maximum ones 
    max_length = 0 # length of the longest substring

    # looping through the array with right pointer
    for r in range(len(arr)):
        if arr[r] == 1:
            max_ones += 1

        # check if the windows size is > k +max_ones, then we update the window size
        while (r-l+1-max_ones) > k:
            if arr[l] == 1:
                max_ones -= 1
            l += 1

        max_length = max(max_length,r-l+1)

    return max_length

# test the function
if __name__=='__main__':
    arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k = 2
    print(length_of_longest_substring(arr,k))

    arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3
    print(length_of_longest_substring(arr,k))
