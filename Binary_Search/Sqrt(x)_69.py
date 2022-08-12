class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        lo=0
        hi=x
        while lo<=hi:
            mid=(lo+hi)//2
            if mid*mid<=x:
                if (mid+1)*(mid+1)>x:
                    return mid
                lo=mid+1
            else:
                hi=mid-1
        