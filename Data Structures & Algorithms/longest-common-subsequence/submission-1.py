class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #its a decision tree
        #when we have a match we increase both indices
        #if not then we decide can ask, what will bring a bigger sequence
        hm = {}

        def rec(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                if (i+1, j+1) in hm:
                    return 1 + hm[(i+1, j+1)]
                ans = 1 + rec(i + 1, j + 1)
                hm[(i + 1, j + 1)] = ans
                return ans

            else:
                left = 0
                right = 0
                if (i + 1, j) in hm:
                    left = hm[(i + 1, j)]
                else:
                    left = rec(i + 1, j)
                    hm[(i + 1, j)] = left

                
                if (i, j + 1) in hm:
                    right = hm[(i, j + 1)]
                else:
                    right = rec(i, j + 1)
                    hm[(i, j + 1)] = right
                
                return max(left, right)
        
        return rec(0,0)