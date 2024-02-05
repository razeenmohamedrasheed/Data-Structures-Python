class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        value = str(num)
        count = 0
        for val in reversed(value):
            if val == "0":
                count += 1
            else:
                break

        if count > 0:
            value = value[:-count]

        return value

        
        