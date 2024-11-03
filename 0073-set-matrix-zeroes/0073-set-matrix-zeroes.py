class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        
        zeros = [[False] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros[i][j] = True
        
        for i in range(rows):
            for j in range(cols):
                if zeros[i][j]:
                    for k in range(cols):
                        matrix[i][k] = 0
                    for k in range(rows):
                        matrix[k][j] = 0