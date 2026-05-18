class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 has to be <= s2
        # we don't care about order
        # we can use a fixed window
        # and each window we check if its a permutation
        # we can slice the string s2
        # 
        if len(s1) > len(s2):
            return False

        h1 = defaultdict(int)
        h2 = defaultdict(int)

        for i in range(len(s1)):
            h1[s1[i]] += 1
            h2[s2[i]] += 1
        m = 0
        print(h1, h2)
        for key, value in h1.items():
            if value == h2[key]:
                m += 1
        
        if h1 == h2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            
            h2[s2[r]] += 1
            h2[s2[l]] -= 1

            if h2[s2[l]] == 0:
                del h2[s2[l]]

            l += 1

            if h1 == h2:
                return True

        return False
           