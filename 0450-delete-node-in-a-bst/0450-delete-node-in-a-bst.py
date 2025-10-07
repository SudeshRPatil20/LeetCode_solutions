# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_min(node):
            current = node
            while current.left is not None:
                current = current.left
            return current
        def delete_helper(root, data):
            if root is None:
                return None
            if data < root.val:
                root.left = delete_helper(root.left, data)
            elif data>root.val:
                root.right = delete_helper(root.right, data)
            else:
                if root.right is None:
                    return root.left
                elif root.left is None:
                    return root.right
                min_val = get_min(root.right)
                root.val = min_val.val
                root.right = delete_helper(root.right, min_val.val)
            return root
        root = delete_helper(root, key)
        return root