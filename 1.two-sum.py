# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc tags=array;hash-table

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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDic = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in numDic:
                return [numDic[diff],i] 
            numDic[x] = i
        return

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,7,11,15], target = 9')
    print('Exception :')
    print('[0,1]Because nums[0] + nums[1] == 9, we return [0, 1].')
    print('Output :')
    print(str(Solution().twoSum([2,7,11,15],9)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,4], target = 6')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().twoSum([3,2,4],6)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [3,3], target = 6')
    print('Exception :')
    print('[0,1]')
    print('Output :')
    print(str(Solution().twoSum([3,3],6)))
    print()
    
    pass
# @lc main=end