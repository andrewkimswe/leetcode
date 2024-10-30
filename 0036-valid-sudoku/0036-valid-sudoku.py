class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

# Time Complexity : O(1), Space Complexity : O(1)    
        
# class Solution:
#   def isValidSudoku(board):
#     rows = [{} for _ in range(9)]       
#     cols = [{} for _ in range(9)]       
#     grids = [{} for _ in range(9)]      
#
#     for i in range(9):
#       for j in range(9):
#         num = board[i][j]
#           if num == '.':
#             continue
#
#         num = int(num)

#         grid_index = (i // 3) * 3 + (j // 3)
#
#         rows[i][num] = rows[i].get(num, 0) + 1
#         cols[j][num] = cols[j].get(num, 0) + 1
#         grids[grid_index][num] = grids[grid_index].get(num, 0) + 1
#
#         if rows[i][num] > 1 or cols[j][num] > 1 or grids[grid_index][num] > 1:
#           return False
#
#    return True
