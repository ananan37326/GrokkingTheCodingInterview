'''

Given an array of unsorted numbers and a target number, 
find a triplet in the array whose sum is as close to the target number as possible, 
return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

'''

# similar approach as Triplet Sum to Zero. In each step we save the difference between the sum and target

def triplet_sum_close_to_target(arr, target_sum):
    #variable to store the smallest difference
    smallest_diff = 99999

    # sort the array
    arr.sort()

    # loop through the array
    for i in range(len(arr)):
        l = i + 1
        r = len(arr) -  1

        while l < r:
            # calculating the current difference
            current_diff = target_sum - arr[i] - arr[l] - arr[r]

            if current_diff == 0:
                # we found the exact target, so return
                return target_sum

            # check for multiple solution
            if abs(current_diff) < abs(smallest_diff) or abs(current_diff) == abs(smallest_diff) and current_diff > smallest_diff:
                # found a triplet with smaller difference
                smallest_diff = current_diff

            if current_diff > 0:
                # we need to increase the current sum
                l += 1

            else:
                # we need to decrease the current sum
                r -= 1

    return target_sum - smallest_diff


# test the function
if __name__ == "__main__":
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
            

