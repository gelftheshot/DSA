class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        
        for i in range(1, len(nums)):
            forward[i] = forward[i -1] * nums[i -1] 
        for i in range(len(nums)-2, -1, -1):
            backward[i] = backward[i + 1] * nums[i + 1]
        return (forward[i] * backward[i] for i in range(len(nums)))