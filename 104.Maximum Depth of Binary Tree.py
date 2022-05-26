# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        depth_of_branch = 0
        deepest_branch = 0
        if root.val == None:
            return 0
        while True:
            current_node = root
            depth_of_branch += 1
            if current_node.left != None:
                current_node = current_node.left
                continue
            if current_node.right != None:
                current_node = current_node.right
                continue
            if (current_node.left == None) & (current_node.right == None):
                if depth_of_branch > deepest_branch:
                    deepest_branch = depth_of_branch
                    continue
                continue
        return deepest_branch
