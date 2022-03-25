class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if k == 0: return nums
        k = k % len(nums)
        l = nums [-k:] + nums[:len(nums) - k]
        for i in range(len(nums)):
            nums[i] = l[i]
