# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftDiam= self.diameterOfBinaryTree(root.left)
        rightDiam= self.diameterOfBinaryTree(root.right)
        diameter= self.height(root.left)+ self.height(root.right)
        
        return max(diameter, max(leftDiam, rightDiam))
    
    def height(self, root):
        if root is None:
            return 0
        left= self.height(root.left)
        right= self.height(root.right)
        return max(left, right)+ 1
       
