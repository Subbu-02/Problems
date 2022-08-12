class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if target==nums[0]:
                return 0
            else:
                return -1
        hi=len(nums)-1
        lo=0
        while lo<=hi:
            mid=(hi+lo)//2
            if target==nums[mid]:
                return mid
            if target>nums[mid]:
                lo=mid+1
            if target<nums[mid]:
                hi=mid-1
        return -1
        