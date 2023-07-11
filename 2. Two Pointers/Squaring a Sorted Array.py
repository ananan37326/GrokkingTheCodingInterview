'''
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]

'''
# since there can be negative numbers in the array, we need to consider the value of their squares
# we will use two pointers at the two ends of the input array
# whichever pointed value squared is highest gets to be put in the output array, then the pointer gets shifted

def make_squares(arr):
    # setting up the pointers
    l, r = 0, len(arr) - 1

    # setting up the output array and the index to traverse
    squares = [ 0 for _ in range(len(arr)) ]
    idx = len(arr) - 1

    # we check the values at both pointer, until they collide
    while l <= r:
        l_square = arr[l] * arr[l]
        r_square = arr[r] * arr[r]

        # if the left square is greater, we put it in the output array and increment the left pointer
        if l_square > r_square:
            squares[idx] = l_square
            l += 1
        # else we put the right square in the output array and decrement the right pointer
        else:
            squares[idx] = r_square
            r -= 1
        # decrement the traversing index
        idx -= 1

    return squares

# test the function
if __name__ == "__main__":
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))