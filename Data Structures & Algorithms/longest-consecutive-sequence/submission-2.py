class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = [c for c in set(nums)]
        s.sort()
        max_len = 1
        stack = []
        for num in s:
            if stack:
                if stack[-1] == num - 1:
                    stack.append(num)
                    max_len = max(max_len, len(stack))
                else:
                    stack = []
                    stack.append(num)
            else:
                stack.append(num)
        
        return max_len
        