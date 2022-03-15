class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1, n+1):
            ref, mod = divmod(i, 2)
            print res[ref], mod, ref
            res.append(res[ref]+mod)
        
        return res
