# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs recursive
        # keep track of the max path sum with nonlocal
        # each node's value is left + node.val + right
        max_path = float('-inf')

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            max_path = max(max_path, left + right + node.val)

            return max(max(left, right) + node.val, 0)

        dfs(root)

        return max_path