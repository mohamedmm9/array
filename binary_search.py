class Solution(object):
    def search(self, nums, target):
        lower=0
        higher=len(nums)-1
        while lower<=higher:
            mid=(lower)+(higher-lower)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                lower=mid+1
            else:
                higher=mid-1
        return -1
