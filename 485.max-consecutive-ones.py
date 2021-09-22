# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#


# @lc tags=array

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
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([0] + list(len(list(i)) for x, i in groupby(nums) if x == 1))
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,0,1,1,1]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,0,1,1,0,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1])))
    print()
    
    pass
# @lc main=end