'''
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
'''

# we will use the same approach as permutation in a string, with the modifications being
# we will keep a substring start index to allow us to return the string window
# we will extend the sliding window and shrink it until the matched length is same as the pattern
# and update the minimum window size

def find_substring(str,pattern):
    #declaring the variables
    l = 0 # left pointer
    min_window = len(str) + 1 # length of the minimum window
    matched = 0 # number of characters matched
    substr_idx = 0 # starting index of the string we are looking for
    char_count = {} # dictionary to keep count of the character of the pattern

    # update the character count of the pattern
    for chr in pattern:
        char_count[chr] = 1 + char_count.get(chr, 0)

    # looping through the string with right pointer
    for r in range(len(str)):
        r_char = str[r] # character at the right of the window

        # if the character is in the pattern, we update the length of the matched and decrement the character count
        if r_char in char_count:
            char_count[r_char] -= 1
            if char_count[r_char] >= 0:
                matched += 1
            

        # shrink the window as long as the length of the pattern is same as matched
        while matched == len(pattern):
            if min_window > r - l + 1:
                min_window = r - l + 1
                substr_idx = l

            # now move the left pointe forward
            l_char = str[l]
            if l_char in char_count:
                if char_count[l_char] == 0:
                    matched -= 1
                char_count[l_char] += 1
            l += 1

    # if the min window is still greater than the length of the string return an empty string otherwise return the substring
    if min_window > len(str):
        return ""
    
    return str[substr_idx:substr_idx+min_window]


# test the function
if __name__ == "__main__":
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdabca", "abc"))
    print(find_substring("adcad", "abc"))