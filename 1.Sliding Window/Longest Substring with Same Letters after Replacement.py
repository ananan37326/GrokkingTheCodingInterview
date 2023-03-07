'''
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

'''

# we will try to keep the character frequency map like before, along with a count for the maximum
# repeating character count

def length_of_longest_substring(str,k):
    # declaring variables
    l = 0 # left pointer
    char_count = {} #dictionary to keep the character counts
    max_repeating_length = 0 #what is the maximum occurrence of a character? we would like to replace other character to this
    max_length = 0 # length of the longest substring 

    # looping through the string with right pointer
    for r in range(len(str)):
        r_char = str[r] # character at the right of the window
        char_count[r_char] = 1 + char_count.get(r_char,0) # updating the character count
        max_repeating_length = max(char_count.values()) # updating the count of maximum repeating chars

        # now we check if the window contains more than k+max_repeating_chars
        while (r-l+1-max_repeating_length > k):
            l_char = str[l]
            char_count[l_char] -= 1
            l += 1

        max_length = max(max_length, r-l+1)

    return max_length

#test the function
if __name__=='__main__':
    str = "aabccbb"
    k = 2
    print(length_of_longest_substring(str,k))

    str = "abbcb"
    k = 1
    print(length_of_longest_substring(str,k))

    str = "abccde"
    k = 1
    print(length_of_longest_substring(str,k))