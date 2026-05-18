class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # excalty once
        # turtle and hare
        # we start both pointer at the start and move them through

        hare = 0
        turtle = 0

        while True:
            hare = nums[nums[hare]]
            turtle = nums[turtle]
            if hare == turtle:
                break
        
        turtle = 0

        while hare != turtle:
            hare = nums[hare]
            turtle = nums[turtle]

        return hare
        
        
        
        
