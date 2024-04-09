class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        reverse = ''.join(reversed(s))
        haha = ''
        for i in range(len(reverse)):
            if reverse[i] != " ":
                haha += reverse[i]
            else:
                break
        return len(haha)