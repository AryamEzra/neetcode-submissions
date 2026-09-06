class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        max_count = 0
        ans = 0
        for k,v in freq.items():
            if v > max_count:
                max_count = v
                ans = k
        return ans

        
        