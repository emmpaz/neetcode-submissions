class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        def backtrack(curList, available):
            ans.append(curList.copy())

            for i in range(len(available)):
                if i > 0 and available[i-1] == available[i]:
                    continue
                else:
                    curList.append(available[i])
                    backtrack(curList, available[i+1:])
                    curList.pop()
        
        backtrack([], nums)
        return ans