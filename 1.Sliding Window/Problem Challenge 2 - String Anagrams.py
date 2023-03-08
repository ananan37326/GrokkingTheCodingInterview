'''
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

'''

# this is the same as permutations of a string problem, except when we find a match we need to store the indices

def find_string_anagrams(str, pattern):
    # declaring variables
    l = 0 # left pointer
    char_count = {} # dictionary to keep character count of the pattern
    matched = 0 # number of matched character so far
    anagrams = [] # list to store the starting indices of the anagrams

    # updating the character count of the pattern
    for chr in pattern:
        char_count[chr] = 1 + char_count.get(chr, 0)

    # looping through the string with right pointer
    for r in range(len(str)):
        r_char = str[r] # character at the right of the window
    
        # check if the character is in the pattern, if yes then decrement the count in the dictionary
        # if that character count is zero, we have one matched character
        # if the number of matched character is equal to the length of the dictionary then we add the starting index to list
        if r_char in char_count:
            char_count[r_char] -= 1
            if char_count[r_char]==0:
                matched += 1
            if matched == len(char_count):
                anagrams.append(l) # the start of the current window

        # now we update the window if the length exceeds that of the pattern
        while (r-l+1) > len(pattern)-1:
            l_char = str[l]
            if l_char in char_count:
                if char_count[l_char] == 0:
                    matched -= 1
                char_count[l_char] += 1

            l+= 1

    return anagrams

# test the function
if __name__=='__main__':
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))