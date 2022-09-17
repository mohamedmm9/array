class Solution(object):
    def findDisappearedNumbers(self, nums):
        l=len(nums)
        
        nums=set(nums)
        
        d=[]

        
        for i in range(1,l+1):
            
            if i not in nums:
                
                d.append(i)

        
        return d
