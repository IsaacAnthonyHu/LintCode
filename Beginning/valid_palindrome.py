
def isPalindrome(s):
    
    
    alpha_list = [x for x in s if x.isalnum()]
    alpha_str = "".join(alpha_list).lower()
    
    
    flip_str = alpha_str[::-1]
    
    if alpha_str == flip_str:
        return True
    else:
        return False
