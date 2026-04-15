class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find an island of Os
        # dfs on it and check if it touches edge of board
        # if doesn't touch, change whole island to Xs

        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X' or (r, c) in visited:
                    continue

                visited.add((r, c))
                island = {(r, c)}
                stack = [(r, c)]
                touching = False

                if (r == 0 or r == len(board) - 1 or
                c == 0 or c == len(board[0]) - 1):
                    touching = True

                while stack:
                    cr, cc = stack.pop()

                    for dr, dc in dirs:
                        nr, nc = cr + dr, cc + dc

                        if (0 <= nr < len(board) and
                            0 <= nc < len(board[0]) and
                            (nr, nc) not in visited and
                            board[nr][nc] == 'O'):
                            visited.add((nr, nc))
                            island.add((nr, nc))
                            stack.append((nr, nc))
                            
                            if (nr == 0 or nr == len(board) - 1 or
                                nc == 0 or nc == len(board[0]) - 1):
                                touching = True

                if not touching:
                    print(island)
                    for i, j in island:
                        board[i][j] = 'X'

                


                    