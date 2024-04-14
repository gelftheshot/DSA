class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        seen = [False] * (n + 1)  # Array for lookup
        for num in nums:
            if 0 < num <= n:
                seen[num] = True
        for i in range(1, n + 1):
            if not seen[i]:
                return i
        return n + 1
        
            
        