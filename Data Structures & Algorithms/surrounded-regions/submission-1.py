class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dfs from border Os
        # mark visited Os as safe
        # flip all other ones

        stack = []
        dirs = [(0, 1), (0, -1), (1, 0), (-1, -0)]
        safe = set()

        # find border Os
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r == 0 or 
                    r == len(board) - 1 or 
                    c == 0 or 
                    c == len(board[0]) - 1) and board[r][c] == 'O':
                        stack.append((r, c))
                        safe.add((r, c))

        while stack:
            cr, cc = stack.pop()
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if (0 <= nr < len(board) and
                    0 <= nc < len(board[0]) and
                    (nr, nc) not in safe and 
                    board[nr][nc] == 'O'):
                    safe.add((nr, nc))
                    stack.append((nr, nc))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X'
