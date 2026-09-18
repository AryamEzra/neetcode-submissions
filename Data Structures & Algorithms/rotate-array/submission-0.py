class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        d = deque(nums)
        d.rotate(k) # built-in, O(n)
        nums[:] = d # slice assignment mutates the caller's list

        