class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def rec(i, cur, total):

            if total == target:
                ans.append(cur.copy())
                return
            if i >= len(nums):
                return
            if total > target:
                return
            
            rec(i+1, cur, total)

            cur.append(nums[i])
            total += nums[i]
            rec(i, cur, total)

            cur.pop()
            total -= nums[i]
        
        rec(0, [], 0)
        return ans