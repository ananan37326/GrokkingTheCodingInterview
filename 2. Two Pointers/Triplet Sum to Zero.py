'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

'''

# sort the array
# iterate the array, for each element X of the array, apply pair with targeted sum with target -X
# handle duplicates

def search_triplets(arr):
    triplets = []

    #sort the aray
    arr.sort()

    # loop through the array
    for i in range(len(arr)):
        # check if duplicate
        if i > 0 and arr[i] == arr[i-1]:
            continue

        # set left and right pointer as well as the target sum for this iteration
        l = i + 1
        r = len(arr) - 1
        target = -arr[i]

        while l < r:
            curr_sum = arr[l] + arr[r]
            if curr_sum == target:
                # found a valid triplet
                triplets.append([arr[i], arr[l], arr[r]])

                # move the pointers
                l += 1

                # move left pointers until we skipped the duplicates
                while l < r and arr[l] == arr[l-1]:
                    l += 1

            elif curr_sum < target:
                # we need to increase the current sum
                l += 1

            else: 
                # we need to decrease the current sum
                r -= 1

    return triplets


# test the function
if __name__ == "__main__":
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))