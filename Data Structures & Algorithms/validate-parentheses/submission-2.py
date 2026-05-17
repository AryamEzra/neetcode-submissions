class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        dict_map = {"(": ")", "{": "}", "[": "]"}

        stack = []
        for char in s:
            if char in ["[", "{", "("]:
                stack.append(char)
            else:
                if stack and dict_map[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
                
        