class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int](
        """
        dic = {}
        new_list = []
        for i,num in enumerate(nums):
            if num not in new_list:
                dic[num] = nums.count(num)
                new_list.append(num)
        li = sorted(dic, key = dic.get, reverse=True)
        return li[0:k]
            