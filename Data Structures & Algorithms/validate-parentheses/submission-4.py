class Solution:
    def isValid(self, s: str) -> bool:
        # if open bracket, append to stack
        # if closing bracket, pop from stack and check if it is the corresponding open
        # if not, return False

        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack:
                return False
            elif char == ')':
                prev = stack.pop()
                if prev != "(":
                    return False
            elif char == ']':
                prev = stack.pop()
                if prev != "[":
                    return False
            elif char == '}':
                prev = stack.pop()
                if prev != "{":
                    return False

        return len(stack) == 0
                    