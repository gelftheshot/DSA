class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x
        if x < 0:
            x = x * -1
    
        m = 10 ** (len(str(x)) - 1)
        reverse = 0
        while x > 0:
            reverse += (x % 10) * m
            m = m / 10
            x = x / 10
        if (reverse > 2 ** 31 -1) or (-1 * reverse < -2**31):
            return 0
        if num < 0:
            return (-1 * reverse)
        return(reverse)
        