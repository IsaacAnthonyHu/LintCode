# Given a string which consists of lowercase or uppercase letters, find the lengthof the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.

# ! Assume the length of giiven string will not exceed 1010.

# Input : s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is '7'.

# Idea: Maximum odd length string in the center, other even length string equally distributed at the both side of the center string.

# So the maximum length should be the total length of the even string length + maximum odd string length

# !!!!! Need to calculate the other odd strings, just use their even part.

class Solution:
"""
@param s: a string which consists of lowercase or uppercase letters
@return: the length of the longest palindromes that can be built
"""
def longestPalindrome(self, s):
    
    unique_chars = set(s)
    
    even_list = [s.count(x) for x in unique_chars if s.count(x)%2==0]
    
    odd_list = [s.count(x) for x in unique_chars if s.count(x)%2==1]
    
    try:
        even_length = sum(even_list)
    except ValueError:
        even_length = 0
    
    try:
        odd_length = sum(odd_list)
        max_odd = max(odd_list)
        odd_minus_length = odd_length-max_odd-len(odd_list)+1
    except ValueError:
        odd_length = 0
        max_odd = 0
        odd_minus_length = 0
    
    return (even_length+max_odd+odd_minus_length)
