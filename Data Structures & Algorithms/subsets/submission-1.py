class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        cur = []
        def rec(i):

            if i >= len(nums):
                ans.append(cur.copy())
                return
            
            rec(i + 1)

            cur.append(nums[i])
            rec(i + 1)
            cur.pop()
        
        rec(0)

        return ans