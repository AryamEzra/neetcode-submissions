class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        cur_max = 0
        
        for n in check:
            if n - 1 not in check:
                cur_len = 0
                cur_num = n
                while cur_num in check:
                    cur_num += 1
                    cur_len += 1
                cur_max = max(cur_len, cur_max)
        return cur_max
            


            

        
        