class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = ''.join(reversed(str(x)))
        if str(x) == reverse:
            return True
        return False