# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # need to check every node, traversal order doesn't matter
        # use dfs, recursion
        # keep track of curr_min and curr_max
        # return a series of "true"s

        def dfs(node, curr_min, curr_max):
            if not node:
                return True
            
            if (node.left and node.left.val >= node.val
                or node.left and node.left.val <= curr_min):
                return False

            if (node.right and node.right.val <= node.val
                or node.right and node.right.val >= curr_max):
                return False

            return (dfs(node.left, curr_min, node.val)
                and dfs(node.right, node.val, curr_max))

        return dfs(root, float("-inf"), float("inf"))