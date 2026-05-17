class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = {'+', '-', '*', '/'}
        for val in tokens:
            if val not in oper:
                stack.append(int(val))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if val == "+":
                    stack.append(val1 + val2)
                elif val == "-":
                    stack.append(val2 - val1)
                elif val == "*":
                    stack.append(val1 * val2)
                elif val == "/":
                    stack.append(int(val2/val1))
            
        return stack[-1]
        