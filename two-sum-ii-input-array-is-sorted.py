class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for i in range(len(numbers)):
            if numbers[i] in d:
                d[numbers[i]].append(i) 
            else:
                d[numbers[i]] = [i]
        
        print d
        res = []
        for x in d:
            if (target - x) in d:
                # print x, d[x]
                if x+x == target and len(d[x]) == 1:
                    continue
                elif x+x == target:
                    r = d[x]
                    res = [r[0]+1, r[1]+1]    
                else:
                    if d[x][0] < d[target-x][0]:
                        res = [d[x][0]+1, d[target-x][0]+1] 
                    else:
                        res = [d[target-x][0]+1, d[x][0]+1] 
            
        # res.sort()
        return res
