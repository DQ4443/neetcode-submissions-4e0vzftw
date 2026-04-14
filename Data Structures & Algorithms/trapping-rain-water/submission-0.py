class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointer
        # water in spot = min of highest pole left and right - height
        left_highest = []
        right_highest = []
        left = 0
        right = 0
        
        l, r = 0, len(height) - 1
        while l < len(height):
            if height[l] > left:
                left = height[l]
            left_highest += [left]
            l += 1

        while r > -1:
            if height[r] > right:
                right = height[r]
            right_highest = [right] + right_highest
            r -= 1

        print(left_highest)
        print(right_highest)

        total = 0
        for i in range(len(height)):
            total += (min(left_highest[i], right_highest[i]) - height[i])

        return total