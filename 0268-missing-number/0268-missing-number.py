class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le  = len(nums) + 1
        lis = []
        nums = sorted(nums)
        for i in range(le):
            lis.append(i)
        for i in range(le-1):
            if lis[i] != nums[i]:
                return lis[i]
        return le - 1