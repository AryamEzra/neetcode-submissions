class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        t = len(temp)
        ans = [0] * t
        for i in range(t):
            while stack and temp[stack[-1]] < temp[i]:
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)
        return ans 
        