class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in check:
                cur = num
                cur_len = 0
                while cur in check:
                    cur_len += 1
                    cur += 1
                max_len = max(max_len, cur_len)
                    
        return max_len

        
                 
        
        