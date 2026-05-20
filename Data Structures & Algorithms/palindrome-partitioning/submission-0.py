class Solution:
    def partition(self, s: str) -> List[List[str]]:
        "a", "b", "c"
        
        res = []
        def search(curr, pos):

                if pos == len(s):
                    res.append(curr.copy())
                
                for i in range(pos, len(s)):
                    t = s[pos:i+1]
                    print(t)
                    if t == t[::-1]:
                        curr.append(t)
                        search(curr, i + 1)
                        curr.pop()
        
        search([], 0)
        return res

