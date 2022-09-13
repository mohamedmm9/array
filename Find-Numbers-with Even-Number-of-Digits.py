class Solution(object):
    def findNumbers(self, nums):
        str_num = map(str, nums)
        count = 0
        for s in str_num:
            if len(s) % 2 == 0:
                count += 1
        return count
        
        ##feitan_codes
