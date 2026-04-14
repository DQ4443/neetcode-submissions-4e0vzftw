class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find correct row, then binary search row

        # find correct row using binary search O(log(n)), then binary
        # search on the element takes O(log(m)) time,
        # summing to log(m * n)

        # find row, need to find which 2 numbers it's between
        row = -1
        low, high = 0, len(matrix) - 1
        while low <= high:
            # skip row search if 1 row
            if len(matrix) == 1:
                row = 0
                break 

            mid = (low + high) // 2

            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] > target:
                high = mid - 1

            else: #
                if matrix[mid][-1] >= target:
                    row = mid
                    break
                low = mid + 1

        print(row)
        # find col
        low, high = 0, len(matrix[row]) - 1
        while low <= high: 
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
        
