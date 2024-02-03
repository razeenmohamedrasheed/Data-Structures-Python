class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        final = 0
        for i in nums:
            if nums.count(i) == 1:
                final += i
        return final
