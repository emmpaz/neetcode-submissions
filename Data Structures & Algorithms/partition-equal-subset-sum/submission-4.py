class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)

        if s % 2 != 0:
            return False
        
        s = s // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            if nums[i] > s:
                return False
            
            dpCopy = dp.copy()
            for j in dp:
                if j + nums[i] == s:
                    return True
                if j + nums[i] < s:
                    dpCopy.add(j+nums[i])
            dp = dpCopy

        return False
