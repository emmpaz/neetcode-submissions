class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)

        if s % 2 != 0:
            return False
        
        s = s // 2


        def rec(i, currSum):
            if currSum == s:
                return True
            if currSum > s:
                return False
            if i == len(nums):
                return False
            
            return rec(i+1, currSum + nums[i]) or rec(i+1, currSum)

        return rec(0, 0)