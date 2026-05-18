class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def backtrack(curList, available):
            if len(available) < 1:
                ans.append(curList.copy())
                return

            for i in range(len(available)):
                curList.append(available[i])
                backtrack(curList, available[:i] + available[i+1:])
                curList.pop()

        backtrack([], nums)
        return ans