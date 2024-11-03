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


# from typing import List

# class Solution:
#    def setZeroes(self, matrix: List[List[int]]) -> None:
#        rows, cols = len(matrix), len(matrix[0])
#        row_zero = False  # 첫 번째 행에 0이 있는지 확인
#        col_zero = False  # 첫 번째 열에 0이 있는지 확인
#
#        # 첫 번째 행과 첫 번째 열에 0이 있는지 확인
#        for i in range(rows):
#            if matrix[i][0] == 0:
#                col_zero = True
#                break
#        for j in range(cols):
#            if matrix[0][j] == 0:
#                row_zero = True
#                break
#
#        # 나머지 행렬을 순회하며, 첫 번째 행과 첫 번째 열을 0 플래그로 사용
#        for i in range(1, rows):
#            for j in range(1, cols):
#                if matrix[i][j] == 0:
#                    matrix[i][0] = 0
#                    matrix[0][j] = 0
#
#        # 첫 번째 행과 열을 참조하여 행과 열을 0으로 설정
#        for i in range(1, rows):
#            if matrix[i][0] == 0:
#                for j in range(1, cols):
#                    matrix[i][j] = 0
#        for j in range(1, cols):
#            if matrix[0][j] == 0:
#                for i in range(1, rows):
#                    matrix[i][j] = 0
#
#        # 첫 번째 행을 0으로 설정
#        if row_zero:
#            for j in range(cols):
#                matrix[0][j] = 0
#
#        # 첫 번째 열을 0으로 설정
#        if col_zero:
#            for i in range(rows):
#                matrix[i][0] = 0
