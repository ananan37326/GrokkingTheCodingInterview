'''
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have 
�
!
n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.

'''

# We keep the character count of the pattern in a hashmap
# then we maintain a sliding window of the same size as the pattern

def find_permutation(str, pattern):
    # declaring variables
    l = 0 # left pointer
    char_count = {} # dictionary to keep count of the characters of the pattern
    matched = 0 # number of matched character

    # update the dictionary
    for chr in pattern:
        char_count[chr] = 1 + char_count.get(chr, 0)

    # looping through the string with right pointer
    for r in range(len(str)):
        r_char = str[r] # character at the righ of the window

        # check if the character is in the pattern
        # if yes, decrement that character count by 1, if the count is 0 then we get one match
        # if the number of match is same as pattern length, we return True
        if r_char in char_count:
            char_count[r_char] -= 1

            if char_count[r_char] == 0:
                matched += 1
        
        if matched == len(char_count):
            return True

        # check if the window size is larger than the length of the pattern
        while (r-l+1) > len(pattern)-1:
            l_char = str[l]
            if l_char in char_count:
                if char_count[l_char]==0:
                    matched -= 1
                char_count[l_char] += 1
            l += 1
        
    return False 

# test the function
if __name__=='__main__':
    print(find_permutation("oidbcaf", "abc"))
    print(find_permutation("odicf", "dc"))
    print(find_permutation("bcdxabcdy", "bcdyabcdx"))
    print(find_permutation("aaacb", "abc"))