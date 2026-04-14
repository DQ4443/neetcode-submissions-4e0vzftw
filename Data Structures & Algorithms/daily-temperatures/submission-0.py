class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # when you pop from the stack, you update
        # the index of the popped value in res since it got its ans

        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            print(temp)
            while stack and temp > stack[-1][0]:
                t, i = stack.pop()

                res[i] = index - i

            stack.append([temp, index])

        while stack:
            t, i = stack.pop()
            res[i] = 0

        return res