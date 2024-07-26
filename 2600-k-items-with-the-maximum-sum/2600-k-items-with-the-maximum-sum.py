class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        result = min(numOnes, k)
        k_reduced = k-numOnes-numZeros
        if k_reduced > 0:
            result += - k_reduced
        return result
        