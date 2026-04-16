# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # helper function to compare two trees
        # dfs the big tree and run the help at every node
        # at every layer, return (left or right or current)

        def compare(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return compare(p.left, q.left) and compare(p.right, q.right)

        def dfs(node):
            if not node:
                return not subRoot
            left = dfs(node.left)
            right = dfs(node.right)

            return left or right or compare(node, subRoot)

        return dfs(root)