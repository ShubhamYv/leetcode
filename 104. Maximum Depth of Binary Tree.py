class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left= self.maxDepth(root.left)
        right= self.maxDepth(root.right)
        return max(left, right)+1
