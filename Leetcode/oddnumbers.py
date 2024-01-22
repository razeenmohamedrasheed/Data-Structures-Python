# Count Odd Numbers in an Interval Range

class Solution:
    def countOdds(self, low: int, high: int) -> int:

        return ((high + 1) >> 1) - (low >> 1)
