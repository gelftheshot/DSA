class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        current = {}
        maxlen = 0
        for r in range(len(s)):
            if s[r] in current and l <= current[s[r]]:
                l = current[s[r]] + 1
            else:
                maxlen = max(maxlen, r - l + 1)
            current[s[r]] = r
        return maxlen
            
        