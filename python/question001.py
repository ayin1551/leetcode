class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, val in enumerate(nums):
            dict[val] = i

        for i, val in enumerate(nums):
            sums = target - val
            if sums in dict and dict[sums] != i:
                return [i, dict[sums]]
        
        return [0,0]
