class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        
        for i, num in enumerate(nums):
            
            for j, number in enumerate(nums):
                if (abs(num - number)) == k and i < j:
                    sum += 1
        return sum
        