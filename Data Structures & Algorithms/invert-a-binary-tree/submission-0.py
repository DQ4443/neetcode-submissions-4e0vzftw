# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # post order dfs
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            # print(node.left, node.right)

            temp = node.left
            node.left = node.right
            node.right = temp

            return node

        return dfs(root)