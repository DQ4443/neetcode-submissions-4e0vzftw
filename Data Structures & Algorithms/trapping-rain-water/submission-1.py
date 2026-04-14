class Solution:
    def trap(self, height: List[int]) -> int:
        # water at index is min(left and right wall) - height at index
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0

        while l < r:
            # left bound
            if height[l] < height[r]:
                res += left_max - height[l]
                l += 1
                left_max = max(left_max, height[l])
            else:
                res += right_max - height[r]
                r -= 1
                right_max = max(right_max, height[r])

        return res