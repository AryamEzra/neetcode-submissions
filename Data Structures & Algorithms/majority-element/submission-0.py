class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        maj = len(nums) // 2

        for k,v in count.items():
            if v > maj:
                return k
        