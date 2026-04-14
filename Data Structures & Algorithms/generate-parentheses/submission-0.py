class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        # if open == close == n: append to res
        # if open < n: append an open and keep going
        # if closed < open: append close and keep going

        def backtracking(openN, closedN):
            if openN == closedN == n:
                sol = "".join(stack)
                res.append(sol)
                return
            
            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtracking(openN, closedN + 1)
                stack.pop()

        backtracking(0, 0)
        return res
        


        return res