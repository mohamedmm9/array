class Solution(object):
    def twoSum(self, nums, target):
        for i,val1 in enumerate(nums):
            for j,val2 in enumerate(nums):
                if val1+val2==target and i!=j:
                    return(i,j)
                    
