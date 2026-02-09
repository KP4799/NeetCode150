"""
Problem: LeetCode 36 - Valid Sudoku

Key Idea:
To determine if a given Sudoku board is valid, we need to check three conditions:
1. Each row must have distinct digits from 1 to 9.
2. Each column must have distinct digits from 1 to 9.
3. Each 3x3 sub-grid must have distinct digits from 1 to 9.

We can use three nested loops to traverse the entire board and use sets to keep track of digits seen in each row, column, and sub-grid.

Time Complexity:
The time complexity of this approach is O(1), as the Sudoku board is always a fixed 9x9 grid. We traverse each cell of the grid once, and the number of cells is constant.

Space Complexity:
The space complexity is O(1) as well because we are using a fixed amount of additional space (sets) that does not depend on the size of the input grid.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    if (
                        (i, num) in seen
                        or (num, j) in seen
                        or (i // 3, j // 3, num) in seen
                    ):
                        return False
                    seen.add((i, num))
                    seen.add((num, j))
                    seen.add((i // 3, j // 3, num))

        return True
        
# x = Solution()
# y = isValidSudoku(board=[["1","2",".",".","3",".",".",".","."],
#         ["4",".",".","5",".",".",".",".","."],
#         [".","9","8",".",".",".",".",".","3"],
#         ["5",".",".",".","6",".",".",".","4"],
#         [".",".",".","8",".","3",".",".","5"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".",".",".",".",".",".","2",".","."],
#         [".",".",".","4","1","9",".",".","8"],
#         [".",".",".",".","8",".",".","7","9"]]) 
# print(y)
