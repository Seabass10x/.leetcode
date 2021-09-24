# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#


# @lc tags=Unknown

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
# 
# 
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p_length = len(palindrome)
        
        if p_length == 1:
            return ""
        
        for i in range(p_length // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
            
        return palindrome[:-1] + 'b'
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('palindrome = "abccba"')
    print('Exception :')
    print('"aaccba"')
    print('Output :')
    print(str(Solution().breakPalindrome("abccba")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('palindrome = "a"')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().breakPalindrome("a")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('palindrome = "aa"')
    print('Exception :')
    print('"ab"')
    print('Output :')
    print(str(Solution().breakPalindrome("aa")))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('palindrome = "aba"')
    print('Exception :')
    print('"abb"')
    print('Output :')
    print(str(Solution().breakPalindrome("aba")))
    print()
    
    pass
# @lc main=end