class Solution(object):
    def duplicateZeros(self, arr):
        arr[:] = [x for i in arr for x in ([i] if i else [0, 0])][:len(arr)]
