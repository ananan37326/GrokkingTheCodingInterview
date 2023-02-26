'''
problem statement

Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

'''

def max_sub_array_of_size_k(k,arr):
    # we will use a sliding window approach

    # declaring variables

    l = 0 #we start the left pointer at the start of the array
    max_sum, sum = 0, 0 # initialzing both with 0

    # moving the right pointer from the start to the end of the array
    for r in range(len(arr)):
        sum += arr[r] # keep adding the rightmost number of the window

        # if r exceeds the window size, we start the calculation
        if r >= k-1:
            max_sum = max(max_sum, sum)

            # remove the leftmost number of the array and move the left pointer one cell
            sum -= arr[l]
            l += 1

    return max_sum


# test the function
if __name__=="__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_sub_array_of_size_k(k,arr))

