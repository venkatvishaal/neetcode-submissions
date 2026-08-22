from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base cases for edge scenarios
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        # Case A: Rob from index 0 to n-2 (exclude last house)
        prev1, curr1 = 0, 0
        for i in range(len(nums) - 1):
            prev1, curr1 = curr1, max(prev1 + nums[i], curr1)
            
        # Case B: Rob from index 1 to n-1 (exclude first house)
        prev2, curr2 = 0, 0
        for i in range(1, len(nums)):
            prev2, curr2 = curr2, max(prev2 + nums[i], curr2)
            
        # Return the maximum of both independent passes
        return max(curr1, curr2)