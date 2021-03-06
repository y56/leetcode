# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
dfs, me
"""
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.d_xy=-1 # depth of x or y
        self.pre=None
        self.parent_xy=None # parent of x or y
        def dfs(root,d):
            
            if root.val==x or root.val==y:
                if self.d_xy==-1: # the first match
                    self.d_xy=d
                    self.parent_xy=self.pre
                    return False
                else: # the second match
                    if self.d_xy==d and self.pre!=self.parent_xy:
                        return True
                    else:
                        return True
            # go deeper
            self.pre=root
            if root.left and root.right:
                return dfs(root.left,d+1) or dfs(root.right,d+1)
            if root.left:
                return dfs(root.left,d+1)
            if root.right:
                return dfs(root.right,d+1)
            
        return dfs(root,0)
"""
dfs, official soln
"""
class Solution:
    def __init__(self):
        self.recorded_depth = None # To save the depth of the first matched node.
        self.is_cousin = False
    def dfs(self, node, depth, x, y):
        if node is None:
            return False
        # Don't go beyond the depth restricted by the first node found.
        if self.recorded_depth and depth > self.recorded_depth:
            return False
        if node.val == x or node.val == y:
            if self.recorded_depth is None:
                # Save depth for the first node.
                self.recorded_depth = depth
            # Return true, if the second node is found at the same depth.
            return self.recorded_depth == depth
        left = self.dfs(node.left, depth+1, x, y)
        right = self.dfs(node.right, depth+1, x, y)
        # self.recorded_depth != depth + 1 would ensure node x and y are not
        # immediate child nodes, otherwise they would become siblings.
        if left and right and self.recorded_depth != depth + 1:
            self.is_cousin = True
        return left or right
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # Recurse the tree to find x and y
        self.dfs(root, 0, x, y)
        return self.is_cousin
"""
bfs, official soln
"""
from collections import defaultdict
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # Queue for BFS
        queue = collections.deque([root])
        while queue:
            siblings = False
            cousins = False
            nodes_at_depth = len(queue)
            for _ in range(nodes_at_depth):
                # FIFO
                node = queue.popleft()     
                # Encountered the marker.
                # Siblings should be set to false as we are crossing the boundary.
                if node is None:
                    siblings = False
                else:
                    if node.val == x or node.val == y:
                        # Set both the siblings and cousins flag to true
                        # for a potential first sibling/cousin found.
                        if not cousins:
                            siblings, cousins = True, True
                        else:
                            # If the siblings flag is still true this means we are still
                            # within the siblings boundary and hence the nodes are not cousins.
                            return not siblings
                    queue.append(node.left) if node.left else None
                    queue.append(node.right) if node.right else None
                    # Adding the null marker for the siblings
                    queue.append(None)
            # After the end of a level if `cousins` is set to true
            # This means we found only one node at this level
            if cousins:
                return False
        return False
