class Solution(object):
    def heightChecker(self, arr):
        count=0
        a=sorted(arr)
        for i,j in zip(arr,a):
            if i != j:
                count+=1
        return count
