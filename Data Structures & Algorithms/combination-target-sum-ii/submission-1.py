class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        #first we sort outside of recursion
        #base case
        #total > target then return
        #if i > len(candidates) then return
        #if total == target then append copy to ans

        #first branch we can continue regular
        #next branch we find the next unique number to go to

        def rec(i, cur, total):
            
            if target == total:
                ans.append(cur.copy())
                return

            if i >= len(candidates): return
            if total > target: return

            #we continue with the same
            cur.append(candidates[i])
            total += candidates[i]
            rec(i+1, cur, total)

            cur.pop()
            total -= candidates[i]
            curNum = candidates[i]
            while i < len(candidates) and curNum == candidates[i]:
                i += 1
            
            rec(i, cur, total)
        
        candidates.sort()
        rec(0, [], 0)

        return ans
        






