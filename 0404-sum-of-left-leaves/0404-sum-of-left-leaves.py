# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leaf = 0

        if root.left and not root.left.left and not root.left.right:
            leaf += root.left.val
        else:
            leaf += self.sumOfLeftLeaves(root.left)
        leaf += self.sumOfLeftLeaves(root.right)
        return leaf