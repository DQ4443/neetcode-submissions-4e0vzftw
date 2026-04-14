class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "[":
                stack.append("]")
            elif char == "{":
                stack.append("}")
            elif char in ")]}":
                if not stack or stack.pop() != char:
                    return False
                

            # for every char, if open, add complement to stack
            # if close, check last bracket in stack
        

            # check if the stack is empty by the end

        return not stack