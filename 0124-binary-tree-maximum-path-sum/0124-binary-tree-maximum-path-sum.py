# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        # 깊이 우선 탐색 함수
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            current_max_path = node.val + left_gain + right_gain
            
            self.max_sum = max(self.max_sum, current_max_path)
            
            return node.val + max(left_gain, right_gain)
        
        # 루트에서 탐색 시작
        dfs(root)
        
        return self.max_sum