class Solution:
    def longestPalindrome(self, s: str) -> str:
        #edge case if equal to one then we just return it back
        #if 2 then we check if both characters are equal
        # if 3 then we start looping through the characters
        

        #loop through each character and extend the sliding window
        # cabaaba
        # caac
        # cca
        
        if len(s) < 2:
            return s
        
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]

        longest = s[0]

        for x in range(len(s) - 1):
            center = s[x]
            r = x
            l = x
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            longest = s[l+1:r] if len(s[l+1:r]) > len(longest) else longest

            r = x+1
            l = x
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            longest = s[l+1:r] if len(s[l+1:r]) > len(longest) else longest
        return longest




