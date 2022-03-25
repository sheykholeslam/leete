class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        d = {}
        
        c = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                d[c] = nums[i]
                nums[i] = 0
                c = c + 1
                
        i = 0
        for x in d:
            nums[i] = d[x]
            i = i+1
        
