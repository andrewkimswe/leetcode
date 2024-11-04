class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 오른쪽 상단에서 시작
        row = 0
        col = cols - 1
        
        while row < rows and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True
            elif current > target:
                col -= 1  # 왼쪽으로 이동
            else:
                row += 1  # 아래로 이동
        return False