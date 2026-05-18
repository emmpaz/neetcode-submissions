class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # output + 1 everytime we get to target
        # first thought is do all possible combinations
        # recursive of flipping the inputs
        # 
        def rec(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            
            
            sub = rec(index+1, total - nums[index])
            add = rec(index+1, total + nums[index])
            return sub + add
        
        return rec(0, 0)