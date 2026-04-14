class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # store the next highest temp, so use decreasing stack
        # storing the coldest day at top, then when a warmer day comes up, pop until no more colder
        # then add to stack
        if not temperatures:
            return []

        coldest = [(temperatures[0], 0)]
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            print(coldest)
            if coldest and temp < coldest[-1][0]:
                coldest.append((temp, i))
                continue
            
            else:
                while coldest and coldest[-1][0] < temp:
                    storedTemp, storedIndex = coldest.pop()
                    res[storedIndex] = i - storedIndex
                coldest.append((temp, i))

        return res