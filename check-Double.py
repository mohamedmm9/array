class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in (arr[:i]+arr[i+1:]):
                if 2*arr[i] == j:
                    return True
        return False
