class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = [x*x for x in nums]
        # Library Solution
        # l.sort()
        # return l
        
        # Manual Solution
        le = len(l)
        min = 0
        for i in range(le):
            if l[i] < l[min]:
                min = i
        
        r = []
        r.append(l[min])
        i = min - 1
        j = min + 1
        while True:
            if i >= 0 and j <= le -1:
                if l[i] > l[j]:
                    r.append(l[j])
                    j = j + 1
                else:
                    r.append(l[i])
                    i = i -1
            elif i >= 0:
                r.append(l[i])
                i = i -1
            elif j <= le -1:
                r.append(l[j])
                j = j + 1
            else:
                break
        return r
