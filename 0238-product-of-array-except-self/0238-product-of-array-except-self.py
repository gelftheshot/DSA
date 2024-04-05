import operator
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resualt = [1] * len(nums)
        for i in range(1, len(nums)):
            resualt[i] = resualt[i - 1] * nums[i - 1]
        mul = 1
        
        for i in range (len(nums) -1, -1, -1):
            resualt[i] *= mul
            mul *= nums[i]
        return resualt
        