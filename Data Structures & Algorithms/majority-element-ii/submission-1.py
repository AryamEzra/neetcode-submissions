class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cur = len(nums) / 3
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        ans = []
        for k,v in freq.items():
            if v > cur:
                ans.append(k)
        return ans 
        