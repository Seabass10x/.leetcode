# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
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
    def tribonacci(self, n: int) -> int:
        F = [0, 1, 1]
        
        for _ in range(n):
            F.append(F[-1] + F[-2] + F[-3])
            
        return F[n]
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().tribonacci(4)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 25')
    print('Exception :')
    print('1389537')
    print('Output :')
    print(str(Solution().tribonacci(25)))
    print()
    
    pass
# @lc main=end