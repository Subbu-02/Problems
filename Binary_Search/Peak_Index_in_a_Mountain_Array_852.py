class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo=0
        hi=len(arr)-1
        while lo<=hi:
            if lo==hi:
                return lo
            mid=(lo+hi)//2
            if arr[mid]>arr[mid+1]:
                if arr[mid]>arr[mid-1]:
                    return mid
                hi=mid-1
            else:
                lo=mid+1