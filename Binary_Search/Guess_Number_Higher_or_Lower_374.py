class Solution:
    def guessNumber(self, n: int) -> int:
        lo=1
        hi=n
        while lo<=hi:
            if lo==hi:
                return lo
            mid=(lo+hi)//2
            if(guess(mid)==-1):
                hi=mid
            elif(guess(mid)==1):
                lo=mid+1
            else:
                return mid