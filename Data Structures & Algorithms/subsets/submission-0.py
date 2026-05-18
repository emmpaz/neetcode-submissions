class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []


        sub = []
        def rec(i):
            
            if i >= len(nums):
                ans.append(sub.copy())
                return
            
            sub.append(nums[i])
            l = rec(i+1)

            sub.pop()
            r = rec(i+1)
        rec(0)
        return ans