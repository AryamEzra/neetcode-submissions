class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = set()
        l = 0
        for n in nums:
            if n not in check:
                check.add(n)
                nums[l] = n
                l += 1
        return l
        