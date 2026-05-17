class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        ans = []
        
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j = i + 1
            k = l - 1
            while j < k:    
                total = nums[j] + nums[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else: 
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        
        return ans
        