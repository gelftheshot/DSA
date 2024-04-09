class Solution(object):
    def divide(self, dividend, divisor):
        # Check for special cases
        if dividend == 0: return 0
        if divisor == 1: return dividend
        if divisor == -1:
            if dividend > -2**31:
                return -dividend
            else:
                return 2**31 - 1
        
        negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple
        
        if negative:
            quotient = -quotient
        
        # Handle overflow
        if quotient < -2**31:
            return -2**31
        elif quotient > 2**31 - 1:
            return 2**31 - 1
        else:
            return quotient