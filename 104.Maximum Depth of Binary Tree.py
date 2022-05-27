# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.deepest_node = 0
        if root == None:
            return self.deepest_node

        def find_depth_of_node(node, depth_of_prev_node):
            if node == None:
                if depth_of_prev_node > self.deepest_node:
                    self.deepest_node = depth_of_prev_node
                return
            depth_of_current_node = depth_of_prev_node + 1
            find_depth_of_node(node.right, depth_of_current_node)
            find_depth_of_node(node.left, depth_of_current_node)

        find_depth_of_node(root, 0)
        return self.deepest_node