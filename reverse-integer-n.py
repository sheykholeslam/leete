class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        if x > pow(2,31) -1:
            return 0
        q, mod = divmod(x, 10)
        r = mod
        while q != 0:
            x = q
            q, mod = divmod(x, 10)
            r = r * 10 + mod
        r = r* sign
        
        if r > pow(2,31) -1 or r < -pow(2,31):
            return 0
        
        return r
