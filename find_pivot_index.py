class Solution:
    def pivotIndex(self, nums):
       
        total_sum = sum(nums)
        sum_left = 0
        sum_right = 0
        total_sum_copy = total_sum
        for i in range(len(nums)):
            sum_right = total_sum_copy - nums[i]
            sum_left = total_sum - sum_right - nums[i]
            if sum_right == sum_left:
                return i
            total_sum_copy = sum_right  
        return -1
