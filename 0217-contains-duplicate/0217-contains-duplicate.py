class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_elem = {}
        for num in nums:
            if num in seen_elem:
                return True
            else:
                seen_elem[num] = 'seen'
        return False
        