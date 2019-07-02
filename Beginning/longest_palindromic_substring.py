class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # Central Expansion
        # Two type: xyzyx or xyzzyx
        
        default_string = ""
        
        for x in range(len(s)):
            
            # odd case
            
            tmp_string = self.find_longest_palindrome(s, x, x)
            
            if len(tmp_string) > len(default_string):
                default_string = tmp_string
            
            # even case
            
            tmp_string = self.find_longest_palindrome(s, x, x+1)
            
            if len(tmp_string) > len(default_string):
                default_string = tmp_string
        
        return default_string
                
    def find_longest_palindrome(self, s, left_index, right_index):
        
        while left_index >= 0 and right_index < len(s):
            
            if s[left_index] == s[right_index]:
                
                left_index -= 1; right_index += 1
            
            else:
                break
            
        return s[left_index+1:right_index]
