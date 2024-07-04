class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_length = 3
        current_row = set()
        columns = [set() for _ in board]
        boxes = [set() for _ in board]

        for i, row in enumerate(board):

            for j, cell in enumerate(row):
                # Heart of the prolem here
                # Each box can be uniquely identified by (row group number // 3) * 3 + (col group number // 3)
                # Box 0 = 0 + 0, Box 2 = 0 + 2, Box 3 = (1) * 3 + (0)
                box_number = (i // 3) * 3 + (j // 3)

                if cell in current_row or cell in columns[j] or cell in boxes[box_number]:
                    return False
                
                if cell != '.':
                    current_row.add(cell)
                    columns[j].add(cell)
                    boxes[box_number].add(cell)

            current_row.clear()

        return True

# Given a 9x9 Sudoku board with some or all cells filled, determine if it
# is valid (no repeated numbers in each row, column and 3x3 box).
#
# Use hashsets (sets) to check for repeated numbers -- if number is already in
# the hashset for its row, column or box, return false.
#
# Hard part is tracking which box each cell belongs to. Notice that every
# row # and col # in a given box gives the same result when floor divided
# by the box length (3). So for all cells in the middle box, (row // 3) == 1
# and (col // 3) == 1. Can identify the box with the tuple (1, 1), or with
# an index with idx = (row // 3) * 3 + (col // 3)
#
# Note we process the input one row at a time, so we only need 1 set to track
# the current row, but for columns and boxes we can only see all numbers after
# iterating over several rows, so we need an indexed collection of sets
# (array is best, since we are identifying col # and box # with numbers)
