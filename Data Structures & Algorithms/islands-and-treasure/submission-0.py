class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # go through all cells to find treasures
        # multi source bfs, updating
        # add to queue when land and unvisited (inf)

        INF = 2147483647
        queue = deque()
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        print(queue)

        while queue:
            cr, cc = queue.popleft()
            

            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if (0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and grid[nr][nc] == INF):
                    print(nr, nc)
                    grid[nr][nc] = grid[cr][cc] + 1
                    queue.append((nr, nc))
        