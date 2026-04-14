class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return None

        numStack = []
        for t in tokens:
            print(t, numStack)
            if t == "+":
                b = numStack.pop()
                a = numStack.pop()
                res = a + b
                numStack.append(res)
            elif t == "-":
                b = numStack.pop()
                a = numStack.pop()
                res = a - b
                numStack.append(res)
            elif t == "*":
                b = numStack.pop()
                a = numStack.pop()
                res = a * b
                numStack.append(res)
            elif t == "/":
                b = numStack.pop()
                a = numStack.pop()
                res = int(a / b)
                numStack.append(res)
            else: # number
                numStack.append(int(t))

        return numStack[0]

            