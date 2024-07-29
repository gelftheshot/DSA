class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxlen = 0
        current = {}
        while i < len(s):
            if s[i] not in current:
                current[s[i]] = i
                i += 1
            else:
                maxlen = max(maxlen, len(current))
                i = current[s[i]] + 1
                current = {}
        return max(maxlen, len(current))
            
        