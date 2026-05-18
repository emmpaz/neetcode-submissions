class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def rec(i, cur, total):

            if total == target:
                ans.append(cur.copy())
                return
            
            if total > target:  return

            if i >= len(nums): return


            rec(i + 1, cur, total)

            cur.append(nums[i])
            rec(i, cur, total + nums[i])
            cur.pop()
        
        rec(0, [], 0)
        return ans