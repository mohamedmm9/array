class Solution(object):
    def sortedSquares(self, nums):
        sq=[]
        for i in range(len(nums)):
            c=nums[i]*nums[i]
            sq.append(c)
            sq.sort()
        return sq
