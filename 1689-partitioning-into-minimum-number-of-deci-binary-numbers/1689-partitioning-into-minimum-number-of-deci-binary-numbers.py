class Solution:
    def minPartitions(self, n: str) -> int:
        val = sorted(n)
        return int(val[-1])