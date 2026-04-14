class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            print(stack)
            if char == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 + num2
                stack.append(res)
            elif char == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 - num2
                stack.append(res)
            elif char == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 * num2
                stack.append(res)
            elif char == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                res = int(num1 / num2)
                stack.append(res)
            else:
                stack.append(int(char))
        return stack[0]
