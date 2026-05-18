class Solution:
    def trap(self, height: List[int]) -> int:
        #if the ends are 0 then we know we can trap water from 
        # the beginning to the first non-zero and the last non-zero to the end
        # to find all windows
        # we continue to expand the window if the right pointer is less than left
        # the problem here is the beginning and end
        # so we can have a temp variable holding the amount of current water
        # and then another variable holding the total water
        # this can resole the end because once we reach the end,
        # if we never find a elevation that is greater or equal to the left one
        # then we know it can't contain the current water so we don't add it
        # 
        if len(height) < 3:
            return 0
        
        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)
  
        total = 0

        for i in range(len(height)):
            l = i - 1
            r = i + 1
            while l >= 0:
                prefix_max[i] = max(prefix_max[i], height[l])
                l -= 1
            
            while r < len(height):
                suffix_max[i] = max(suffix_max[i], height[r])
                r += 1

        for i in range(len(height)):
            t = min(suffix_max[i], prefix_max[i]) - height[i]
            total += max(0, t)
        
        return total
