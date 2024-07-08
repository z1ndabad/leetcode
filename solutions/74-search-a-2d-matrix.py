class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def idx_to_matrix(i, columns) -> (int, int):
            return (i // columns, i % columns)

        row_count = len(matrix)
        if row_count == 0:
            return False

        col_count = len(matrix[0])
        lo, hi = 0, row_count * col_count - 1

        while lo < hi:
            mid_index = lo + (hi - lo) // 2
            row, col = idx_to_matrix(mid_index, col_count)
            mid_element = matrix[row][col]

            if mid_element == target:
                return True
            elif mid_element < target:
                lo = mid_index + 1
            else:
                hi = mid_index
        
        final_row, final_col = idx_to_matrix(lo, col_count)
        return True if matrix[final_row][final_col] == target else False

# Given a matrix of integers size m*n, with the properties that
# every row is sorted in non-decreasing order and the first integer
# of each row is greater than the last of the previous row, return
# whether the target value is in the matrix
#
# Classic binary search. The input matrix is basically a sorted array,
# split into subarrays of equal length.
#
# NOTICE that if we imagine all the matrix values in a 1d array, an index
# idx of that array maps to the matrix cells with:
# row == idx // column_count, column == idx % column_count
#
# AND the index of the final cell in the matrix is rows * columns - 1.
#
# Set up binary search, lo = 0, hi = rows * columns - 1.
# Calculate midpoint index as normal, then map the index into a matrix cell.
# Once loop is done, hi and lo both point to the result. Return
# true if the element at lo/hi is the result.
