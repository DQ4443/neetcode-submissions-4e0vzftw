# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # need to traverse every node in any way
        # dfs recursion
        # need to keep track of max and min allowed for all nodes
        # return a series of "True"s

        def dfs(node, curr_min, curr_max):
            if not node:
                return True

            if node.val <= curr_min:
                return False
            if node.val >= curr_max:
                return False

            return (dfs(node.left, curr_min, node.val)
                and dfs(node.right, node.val, curr_max))

        return dfs(root, float("-inf"), float("inf"))