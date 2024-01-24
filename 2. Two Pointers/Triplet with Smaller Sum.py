'''

Given an array arr of unsorted numbers and a target sum, count all triplets in it such that 
arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Example 1:

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

'''

# we will use the same approach as the triplet sum to zero
def triplet_with_smaller_sum(arr, target):
    # sort the array
    arr.sort()
    
    # set the count
    count = 0
    
    # loop through the array
    for i in range(len(arr)):
        # set the left and right pointer
        l = i + 1
        r = len(arr) - 1
        
        # set the target sum
        target_sum = target - arr[i]
        
        while l < r:
            curr_sum = arr[l] + arr[r]
            if curr_sum < target_sum:
                # we found a triplet
                count += r - l
                
                # move the left pointer
                l += 1
                
                # move the left pointer until we skip the duplicates
                while l < r and arr[l] == arr[l-1]:
                    l += 1
            else:
                # we need to decrease the current sum
                r -= 1
    
    return count

# test
print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))