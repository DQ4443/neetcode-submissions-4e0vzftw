class Solution:
    def decodeString(self, s: str) -> str:
        # use stack to store state, pop from stack when you see ]
        # start making the newChar, keep buiding until you see [
        # then multiply and append the result

        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
                continue

            newStr = ''
            while stack and stack[-1] != '[':
                prev = stack.pop()
                newStr = prev + newStr
            _ = stack.pop()
            # construct num
            num = ''
            while stack and stack[-1].isnumeric():
                digit = stack.pop()
                num = digit + num
            newStr *= int(num)
            stack.append(newStr)

        res = ''
        for char in stack:
            res += char

        return res
