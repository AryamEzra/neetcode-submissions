class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = n * (n+1) // 2
        cur = sum(nums)
        return summ - cur

        