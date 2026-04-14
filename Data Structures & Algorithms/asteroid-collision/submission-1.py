class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # use stack
        # if num is positive, add to stack and continue
        # else (if neg): pop pos and collide, while loop until neg is gone or stack is empty
        # then append the result (big pos or that neg) back unto stack

        stack = []
        for ast in asteroids:
            while ast < 0 and stack:
                prev = stack.pop()
                if prev < 0:
                    stack.append(prev)
                    break
                if ast + prev > 0:
                    ast = prev
                elif ast + prev == 0:
                    ast = 0
            if ast != 0:
                stack.append(ast)
        return stack
            
            