class Solution:
    def scoreOfString(self, s: str) -> int:
        sum1 = 0
        for i in range(len(s) - 1):
            dif = abs(ord(s[i]) -ord(s[i+1]) )
            sum1 += dif
        return sum1