# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal, dfs
        # increment counter, in middle
        # return when counter == k

        def inorder(node, count):
            if not node:
                return count, None

            count, res = inorder(node.left, count)
            if res is not None:
                return count, res

            count += 1
            if count == k:
                return count, node.val

            count, res = inorder(node.right, count)
            if res is not None:
                return count, res

            return count, None

        _, ans = inorder(root, 0)
        return ans