class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg = 0
        end = len(nums) -1
        i = (beg + end) // 2
        while True:
            if nums[i] == target:
                return i
            if beg == end:
                if nums[i] > target:
                    return i
                else:
                    return i+1
            if nums[i] > target:
                end = i
            else:
                beg = i+1
            i = (beg + end) // 2
                
