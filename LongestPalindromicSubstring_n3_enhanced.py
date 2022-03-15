class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        oc = {}
        r = range(len(s))
        r.reverse()
        for i in r:
            if s[i] in oc:
                oc[s[i]].append(i) 
            else:
                oc[s[i]] = [i]
        max = 0
        rtype = ""
        for i in range(len(s)):
            for t in oc[s[i]]:
                # print i, t
                if t - i >= max:
                    fail = False
                    # print s[i:t+1]
                    for m in range((t - i)/2 + 1):
                        if s[i+m] != s[t-m]:
                            fail = True
                    if fail == False:
                        rtype = s[i:t+1]
                        max = t - i
                        
        return rtype
