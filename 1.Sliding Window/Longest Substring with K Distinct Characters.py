''' 
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

'''

def longest_substring_with_k_distinct(str,k):
    # declaring variables
    l = 0 # left pointer starting at index 0

    max_length = 0 # length of the longest substring

    freq = {} # a dictionary to keep the count of the characters

    # looping through the string with right pointer
    for r in range(len(str)):
        # character at the right pointer position
        rch = str[r]

        # update the character count in the dictionary
        freq[rch] = 1 + freq.get(rch,0)

        # shrink the window until the length of the dictionary
        # gets under k
        while len(freq) > k:
            # character at the left pointer position
            lch = str[l]

            # remove the left most character of the window
            freq[lch] -= 1
            if freq[lch] == 0:
                freq.pop(lch)

            # move the left pointer
            l += 1
        
        # update the length
        max_length = max(max_length, r-l+1)

    return max_length

# test the function
if __name__=="__main__":
    str = "araaci"
    k = 3
    print(longest_substring_with_k_distinct(str,k))


