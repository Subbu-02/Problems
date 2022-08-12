class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo=0
        hi=len(nums)-1
        if target>nums[hi]:
            return hi+1
        elif target<nums[lo]:
            return 0
        while lo<=hi:
            mid=(lo+hi)//2
            if target==nums[mid]:
                return mid
            if target<nums[mid]:
                if target>nums[mid-1]:
                    return mid
                else:
                    hi=mid-1
            else:
                if target<nums[mid+1]:
                    return mid+1
                else:
                    lo=mid+1