class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        y = len(nums1)
        if len(nums1) % 2 != 0:
            y = int(y/2)
            return(nums1[y])
        else:
            x = int(y/2 - 1)
            y = int(y/2)
            result = nums1[x] + nums1[y]
            return result / 2
            
        
        
        