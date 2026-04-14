class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = []
        for i in range(len(speed)):
            array.append((position[i], speed[i]))

        array.sort(key=lambda x: x[0], reverse=True)

        stack = []

        for pos, spd in array:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)