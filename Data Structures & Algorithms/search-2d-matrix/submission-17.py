class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary serach to find the right row, then binary search to find the right column

        if not matrix: return False

        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                break

        row = mid

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True

        return False 