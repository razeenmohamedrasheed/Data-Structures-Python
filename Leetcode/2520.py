class Solution:
    def countDigits(self, num: int) -> int:
        value = str(num)
        count = 0
        for i in value:
            if num % int(i) == 0:
                count += 1
        return count