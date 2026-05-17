class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in set(nums):
            return -1
            
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1

        return -1
        