class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # at every position can choose to add open or close
        # only restriction is that at any point, #close <= #open

        res = []

        def backtrack(i, curr, op, cls):
            if i == n * 2:
                res.append(curr[:])
                return 

            if i > n * 2:
                return

            # close case
            if cls < op:
                backtrack(i + 1, curr + ")", op, cls + 1)

            # open case
            if op < n:
                backtrack(i + 1, curr + "(", op + 1, cls)

        backtrack(0, '', 0, 0)
        
        print(res)
        return res