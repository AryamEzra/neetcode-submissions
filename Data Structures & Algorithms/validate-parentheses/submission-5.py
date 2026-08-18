class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openn = {'{', '[', '('}
        for c in s:
            if c in openn:
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    if (c == "}" and top == "{") or (c == "]" and top == "[") or (c == ")" and top == "("):
                        continue
                    else:
                        return False
                else:
                    return False
        if stack:
            return False    
        return True
        
        