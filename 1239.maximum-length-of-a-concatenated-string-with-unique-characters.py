# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
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
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(charSet, s):
            prev = set()
            for c in s:
                if c in charSet or c in prev:
                    return True
                prev.add(c)
            return False

        def backtrack(i):
            if i == len(arr):
                return len(charSet)

            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i + 1)) # dont concatenate arr[i]

        return backtrack(0)
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = ["un","iq","ue"]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().maxLength(["un","iq","ue"])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('arr = ["cha","r","act","ers"]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maxLength(["cha","r","act","ers"])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('arr = ["abcdefghijklmnopqrstuvwxyz"]')
    print('Exception :')
    print('26')
    print('Output :')
    print(str(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"])))
    print()
    
    pass
# @lc main=end