'''
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

'''

# maintain two pointers. Since this is a sorted array
# if the sum of numbers pointed by two pointers is greater, shift right pointer to left
# if the sum is less, shift left pointer to right

def pair_with_target_sum(arr, target_sum):
    # initializing pointers
    l,r = 0, len(arr) - 1

    # we check the sum until the left and right pointers cross each other
    while l<=r:
        sum = arr[l] + arr[r]

        if sum == target_sum: 
            # we found the target sum
            return [l,r]
        elif sum > target_sum:
            # we need to reduce the sum, so we move the right pointer to left
            r -= 1
        else:
            # we need to increase the sum, so we move the left pointer to right
            l += 1
        
    # if we reach here, it means we did not find the target sum
    return [-1,-1]

# test the function
if __name__ == "__main__":
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))

