class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            j = n-i
            if '0' not in str(i) and '0' not in str(j):
                if int(i) + int(j) == n:
                    return [i,j]
        return []
                