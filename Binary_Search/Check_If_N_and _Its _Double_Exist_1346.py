class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i]==0:
                for j in range(i+1, len(arr)):
                    if arr[j] == 0:
                        return True
            if arr[i]!=0 and (arr[i]*2 in arr):
                return True
        return False