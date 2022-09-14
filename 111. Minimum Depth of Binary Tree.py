class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return max(self.minDepth(root.left), self.minDepth(root.right))+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
