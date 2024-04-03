class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = {}
        
        for i,n in enumerate(nums):
            diff = target - n
            
            if diff  in arr:
                return[arr[diff], i]
            arr[n] = i
                    