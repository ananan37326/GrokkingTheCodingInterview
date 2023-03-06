'''
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".

''' 

# we will keep a dictionary like before, except as soon as some character get repeated we update the window

def non_repeat_substring(str):
    # declaring variables
    l = 0 # left pointer
    max_length = 0 # keep count of the max length of the substring
    idx_map = {} # a dictionary to keep track of the last occurence of a character

    # looping through the string with right pointer
    for r in range(len(str)):
        r_char = str[r] # character at the rightmost point of the window
        
        # check if the character has already occurred or not, if yes then update the window
        if r_char in idx_map:
            # check if the left pointer is ahead of the last occurrence of r_char or not, if not then update left pointer
            l = max(l, idx_map[r_char]+1)

        # update the character index
        idx_map[r_char] = r 

        # update the max length
        max_length = max(max_length, r-l+1)

    return max_length 


# test the function
if __name__=="__main__":
    str = "aabccbb"
    print(non_repeat_substring(str))

    str = "abbbb"
    print(non_repeat_substring(str))

    str = "abccde"
    print(non_repeat_substring(str))