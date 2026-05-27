class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) < 1: return []

        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        ans = []
        def rec(curword, pos):

            if pos >= len(digits):
                ans.append(curword)
                return
            
            for i in dic[digits[pos]]:
                rec(curword + i, pos + 1)
        
        rec("", 0)
        return ans

