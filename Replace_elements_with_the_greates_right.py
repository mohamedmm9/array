class Solution:
    def replaceElements(self, arr):
        l=len(arr)
        ans=[]
        for i in range(l-1):
 
            arr_r_max=max(arr[i+1:])
            ans.append(arr_r_max)
        ans.append(-1)
        return ans
