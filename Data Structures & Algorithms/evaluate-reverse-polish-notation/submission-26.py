class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack to store calculated numbers to the top

        stack = []

        for char in tokens:
            print(char, stack)
            if char in "+-*/":
                b = stack.pop()
                a = stack.pop() 

                if char == "+":
                    res = a + b
                    stack.append(res)
                elif char == "-":
                    res = a - b
                    stack.append(res)
                elif char == "*":
                    res = a * b
                    stack.append(res)
                elif char == "/":
                    res = int(a/b)
                    stack.append(res)

                print(res)
            else:
                stack.append(int(char))


        return stack[0]