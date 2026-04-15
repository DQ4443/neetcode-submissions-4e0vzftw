class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # graph traversal with dfs, stack
        # keep counter
        # traverse graph and mark visited as 0, increment
        
        counter = 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '0':
                    continue

                counter += 1
                stack = [(r, c)]
                grid[r][c] = '0'

                while stack:
                    cr, cc = stack.pop()

                    for dr, dc in dirs:
                        nr, nc = cr + dr, cc + dc
                        
                        if (
                            0 <= nr < len(grid) and
                            0 <= nc < len(grid[0]) and
                            grid[nr][nc] == '1'
                        ):
                            grid[nr][nc] = '0'
                            stack.append((nr, nc))

        return counter
                            
