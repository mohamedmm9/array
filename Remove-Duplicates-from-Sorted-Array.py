
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n

        i = 0
        j = i+1    
        while j <= n-1:
            if nums[j] != nums[i]:  
                nums[i+1] = nums[j]
                i += 1
            j += 1          
        return i + 1
