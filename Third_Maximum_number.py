class Solution(object):
    def thirdMax(self, nums):
       
        
        if nums is None:
            return 
        
        n = list(set(nums))
        cp = n
        if len(n)<=2:
            return max(n)
        else: 
            i=0
            while i<2:
                cp.remove(max(cp))
                i+=1
            
        return max(cp)
