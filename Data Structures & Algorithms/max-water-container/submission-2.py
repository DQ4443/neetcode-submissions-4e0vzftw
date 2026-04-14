class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointer, increment pointer with the smaller height

        if not heights:
            return 0

        res = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            res = max(res, water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res