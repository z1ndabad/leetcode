# Backtracking is a technique for finding the CORRECT SERIES OF CHOICES
# to solve a problem. When a choice is incorrect, we need to BACKTRACK to
# an earlier decision point and make a different choice.
#
# Consider finding a path out of a maze. We could (non-optimally) try to
# traverse each path until we hit a dead end. On hitting a dead end, we
# backtrack to the previous node and try visiting a different neighbor. If
# all neighbors are visited, we backtrack again until we reach a node with an
# unvisited neighbor.
#
# This is the same as a graph DFS with a visited collection --
# THE RECURSION DOES THE BACKTRACKING IMPLICITLY, because the call stack
# contains sequential application states -- exiting a function call returns
# us to the next call down in the stack.
#
# We always have: 
# - Goal -- confirms we have reached the solution
# - Choices -- choosing one path or another, choosing some combination of items
# - Constraints -- can move within a grid, must move around rocks, 
#
# Ex: Sudoku solver (exponential time oh no)
# - Goal: reach the end of the last row -- BASE CASE at top of function
# - Core choice/decision space: fill a given cell with 1-9 -- FOR LOOP to exhause choices
# - If filling with 1-9 makes the row, column and subgrid valid, 
#   progress to the next cell (recursively call solve(row, col+1, ...)) -- RECURSIVE CALL
# - If no value 1-9 results in a valid cell, reset the current cell to empty -- RESET STATE
#
# This is the layout of a recursive function for solving a Sudoku board with
# backtracking. Note the solution above sucks and will be O(m^n), exponential
