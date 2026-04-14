class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on first number of row until you find the smallest number bigger than target
        # target must be on the previous row
        # once found row, binary search in row
        # edge case for matrix is just a vertical vector (list is len(0)), handle only if problematic
        if not matrix:
            return False

        # find row
        top, bottom = 0, len(matrix) - 1
        row = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] > target:
                if 0 <= mid - 1 and matrix[mid - 1][0] < target:
                    row = mid - 1
                    break
                bottom = mid - 1
            elif matrix[mid][0] < target:
                if mid + 1 < len(matrix) and matrix[mid + 1][0] > target:
                    row = mid
                    break
                top = mid + 1
            else:
                return True

        # find col
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True

        return False