class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            current = nums[i]
            l, r = i + 1, n - 1

            while l < r:
                res = current + nums[l] + nums[r]
                if res < 0:
                    l += 1
                elif res > 0:
                    r -= 1
                else:
                    result.append([current, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return result