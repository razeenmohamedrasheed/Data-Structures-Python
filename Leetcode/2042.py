class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0
        for i in s.split():
            if i.isdigit():
                num = int(i)
                if num <= prev:
                    return False
                prev = num

        return True
            