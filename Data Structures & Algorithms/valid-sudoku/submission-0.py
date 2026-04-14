class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check if row contains duplicates
        # check if column contains duplicates
        # check if box contains duplicates

        # check contain duplicate for len(list) == len(set(list))

        row_lists = defaultdict(list)
        col_lists = defaultdict(list)
        box_lists = defaultdict(list)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                # print(row_lists)
                # print(col_lists)
                # print(box_lists)
                if num in row_lists[row] or num in col_lists[col] or num in box_lists[(row//3, col//3)]:
                    return False
                row_lists[row].append(num)
                col_lists[col].append(num)
                box_lists[(row//3, col//3)].append(num)

        return True