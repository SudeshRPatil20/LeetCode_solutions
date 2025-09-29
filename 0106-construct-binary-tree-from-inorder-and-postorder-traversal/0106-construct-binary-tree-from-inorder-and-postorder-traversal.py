# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def construct_tree_from_inorder_postorder(inor, postord, inS, inE, poS, poE):
    if inS> inE or poS > poE:
        return None
    root_data = postord[poE]
    root = TreeNode(root_data)

    rootInorderIndex = -1
    for i in range(inS, inE+1):
        if inor[i] == root_data:
            rootInorderIndex = i
            break
    if rootInorderIndex == -1:
        print("Root not found")
    
    LinS= inS
    LinE= rootInorderIndex - 1
    LpoS= poS
    LpoE= LpoS + (LinE - LinS)

    RlnS= rootInorderIndex + 1
    RlnE= inE
    RpoS= LpoE + 1
    RpoE= poE - 1
    
    root.left = construct_tree_from_inorder_postorder(inor, postord, LinS, LinE, LpoS, LpoE)
    root.right = construct_tree_from_inorder_postorder(inor, postord, RlnS, RlnE, RpoS, RpoE)

    return root

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return construct_tree_from_inorder_postorder(inorder, postorder, 0, len(inorder)-1, 0, len(inorder)-1)