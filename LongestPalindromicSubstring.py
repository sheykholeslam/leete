class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        ps = []
            
        for i in range(len(s)):
            ps.append([i,i])
            res = [i,i]
        
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                ps.append([i-1, i])
                res = [i-1, i]
        for p in ps:
            beg = p[0] - 1
            end = p[1] + 1
            if beg>= 0 and  end< len(s):
                if s[beg] == s[end]:
                    ps.append([beg, end])
                    res = [beg, end]
                    # print res
        
        return s[res[0]:res[1]+1]

