class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo=1
        hi=max(piles)
        def eatHours(m: int) -> int:
            sum=0
            for x in piles:
                sum+=(x-1)//m+1
            return sum
        while lo<hi:
            m=(lo+hi)//2
            if eatHours(m)<=h:
                hi=m
            else:
                lo=m+1
        return lo