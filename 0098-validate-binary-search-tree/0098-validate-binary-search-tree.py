# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lef=float('-inf'), rig=float('inf')):
            # Base case: empty tree is valid
            if node is None:
                return True

            # Current node must satisfy the BST property
            if not (lef < node.val < rig):
                return False

            # Recursively validate left and right subtrees
            return helper(node.left, lef, node.val) and helper(node.right, node.val, rig)

        return helper(root)
