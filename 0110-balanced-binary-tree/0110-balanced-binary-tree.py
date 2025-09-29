# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balence(root):
            if root is None:
                return True, 0
            
            left_balence, left_height=check_balence(root.left)
            if not left_balence:
                return False, 0
            
            right_balence, right_height = check_balence(root.right)
            if not right_balence:
                return False, 0
            
            balenced=abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)

            return balenced, height
        balenced, _ = check_balence(root)
        return balenced