class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        r = ""
        res = {}
        
        l = 0
        o = 'p'
        for r in range(numRows):
            res[r] = []
            
        for i in range(len(s)):
            res[l].append(s[i])
            if o == 'p' and l < numRows -1:
                l += 1
            elif o == 'm' and l > 0:
                l -= 1
            if l == numRows -1:
                o = 'm'
            if l == 0:
                o = 'p'
        result = ""
        for k in res:
            for l in res[k]:
                result += l
        return result
            
                
                
