class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # multi source dfs traverse pacific, then atlantic
        # add all boundary blocks for pacific and atlantic at start
        # look for > grid[cr][cc] for dfs
        # append overlap

        pacific = []
        atlantic = []
        res = []
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        pacific_valid = set()
        atlantic_valid = set()

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    pacific.append((r, c))
                    pacific_valid.add((r, c))
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    atlantic.append((r, c))
                    atlantic_valid.add((r, c))

        print(pacific_valid, atlantic_valid)

        while pacific:
            visited = set()
            cr, cc = pacific.pop()
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if (0 <= nr < len(heights) and
                    0 <= nc < len(heights[0]) and
                    (nr, nc) not in pacific_valid and
                    heights[nr][nc] >= heights[cr][cc]):
                    pacific.append((nr, nc))
                    pacific_valid.add((nr, nc))

        while atlantic:
            cr, cc = atlantic.pop()
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if (0 <= nr < len(heights) and
                    0 <= nc < len(heights[0]) and
                    (nr, nc) not in atlantic_valid and
                    heights[nr][nc] >= heights[cr][cc]):
                    atlantic.append((nr, nc))
                    atlantic_valid.add((nr, nc))

        print(pacific_valid, atlantic_valid, pacific_valid & atlantic_valid)

        return [list(x) for x in pacific_valid & atlantic_valid]
            


