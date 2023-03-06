'''
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

'''

# This is basically same as 'Longest Substring with K Distinct Character' with k=2

def fruits_into_baskets(fruits):
    # declaring variables
    l = 0 # the left pointer
    fruits_counter = {} # dictionary to keep count of the fruits

    max_fruits = 0 # number of maximum fruits to be put in the baskets

    # looping through the list with right pointer
    for r in range(len(fruits)):
        r_fruit = fruits[r]

        fruits_counter[r_fruit] = 1 + fruits_counter.get(r_fruit,0)

        # now shrink the sliding window until there are 2 fruits left
        while len(fruits_counter) > 2:
            l_fruit = fruits[l]

            fruits_counter[l_fruit] -= 1

            if fruits_counter[l_fruit] == 0:
                fruits_counter.pop(l_fruit)
            
            l += 1

        # update the max number of fruits
        max_fruits = max(max_fruits, r-l+1)

    return max_fruits


#test the function
if __name__=="__main__":
    fruits = ['A', 'B', 'C', 'A', 'C']
    print(fruits_into_baskets(fruits))

    fruits = ['A', 'B', 'C', 'B', 'B', 'C']
    print(fruits_into_baskets(fruits))