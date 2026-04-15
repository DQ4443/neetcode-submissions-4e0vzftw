"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # deep copy requires a old_to_new map
        # dfs traverse through node neighbors
        # mark on push

        if not node:
            return 

        old_to_new = {node: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()
            for neigh in curr.neighbors:
                if neigh not in old_to_new:
                    old_to_new[neigh] = Node(neigh.val)
                    stack.append(neigh)
                
                old_to_new[curr].neighbors.append(old_to_new[neigh])

        return old_to_new[node]