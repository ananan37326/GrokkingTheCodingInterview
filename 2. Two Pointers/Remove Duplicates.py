'''
Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

'''
# since this is a sorted array, duplicated will be in successive positions. 
# We keep two pointers . one for the resultant array index and other for traversing the array
# if the numbers are not same, we put the traversing element in resultant index and increment both pointers
# else just increment the traversing pointer

def remove_duplicates(arr):
    # defining the pointers
    idx = 1 # since we return the length of the final array, we keep track using this pointer
    i = 1 # we traverse using this index
    
    for i in range(1, len(arr)):
        # check if the last non duplicate number i.e. arr[idx-1] is same as arr[i]
        if arr[idx-1] != arr[i]:
            arr[idx] = arr[i]
            idx += 1
        
    return idx 

# test the function
if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
    print(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
    print(remove_duplicates([1, 1, 1, 1, 2, 2, 2, 2, 3, 3]))
    print(remove_duplicates([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4]))
    print(remove_duplicates([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]))

