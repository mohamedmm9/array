class Solution(object):
    def sortedSquares(self, nums):
        s=[]
        for i in nums:
            i=i*i
            s.append(i)
            s=sorted(s)
        return s
