class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero = ord('0')
        hero = ord('9')
        res = 0
        sign = 1;
        dig = False
        let = False
        sig = False
        for l in s:
            n = ord(l)
            if l == ' ' and dig == False and sig == False:
                continue;
            elif l == '+' and sig == False and let == False and dig == False:
                sig = True
            elif l == '-' and sig == False and let == False and dig == False:
                sig = True
                sign *= -1
            elif n >= zero and n <= hero and let == False:
                res = res * 10 + (n-zero)
                dig = True
            elif dig == True or let == True:
                dig = False
                let = True
                continue
            else:
                return 0
        res = res * sign
        
        max = pow(2, 31) -1
        min = pow(-2, 31)
        if res > max:
            res = max
        if res < min:
            res = min
            
        return res
