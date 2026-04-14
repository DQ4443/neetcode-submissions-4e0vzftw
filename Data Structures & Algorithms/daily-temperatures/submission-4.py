class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically decreasing stack
        # pop when warmer comes up, store colder in stack

        temp_stack = [] # (temp, idx)
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1][0]:
                t, idx = temp_stack.pop()
                res[idx] = i - idx

            temp_stack.append((temp, i))

        print(res)
        return res