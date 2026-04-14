class Solution:
    def trap(self, height: List[int]) -> int:
        # water at every index is min(left wall, right wall) - self
        
        left_walls = [0] * len(height)
        curr_lw = 0
        for i in range(len(height)):
            left_walls[i] = curr_lw
            curr_lw = max(curr_lw, height[i])

        right_walls = [0] * len(height)
        curr_rw = 0
        for j in range(len(height) - 1, -1, -1):
            right_walls[j] = curr_rw
            curr_rw = max(curr_rw, height[j])

        res = 0
        for i in range(len(height)):
            vol = min(left_walls[i], right_walls[i]) - height[i]
            if vol > 0:
                res += vol

        return res