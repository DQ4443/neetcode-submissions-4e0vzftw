class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # graph traversal, use dfs with stack
        # mark as visited with setting to 0
        # keep track of max_area and curr_area

        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue

                stack = [(r, c)]
                curr_area = 1
                grid[r][c] = 0


                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in dirs:
                        nr, nc = cr + dr, cc + dc

                        if (0 <= nr < len(grid) and
                            0 <= nc < len(grid[0]) and
                            grid[nr][nc] == 1):
                            curr_area += 1
                            stack.append((nr, nc))
                            grid[nr][nc] = 0


                max_area = max(max_area, curr_area)

        return max_area