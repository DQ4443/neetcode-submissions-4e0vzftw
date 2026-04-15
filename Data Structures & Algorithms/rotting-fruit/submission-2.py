class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs, starting with rotten fruits
        # keep track of the fresh fruits count

        q = deque()
        fresh = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        # iterate through to populate rotten and fresh count
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # print(q)

        # multi source bfs, 1 level at a time
        while q and fresh > 0:
            for _ in range(len(q)):
                cr, cc = q.popleft()

                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc

                    if (0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

                
            # print(grid)
            res += 1

        return -1 if fresh else res

