# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs, recursive
        # keep track of longest path so far
        # path at any node is left + right

        def dfs(node):
            if not node:
                return 0, 0 

            left, left_max = dfs(node.left)
            right, right_max = dfs(node.right)

            diam = 1 + max(left, right)
            max_diam = max(left_max, right_max, left + right)
            return diam, max_diam

        return dfs(root)[1]