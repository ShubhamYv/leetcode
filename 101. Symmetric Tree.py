class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(p,q):
            if p== None and q== None:
                return True
            if p== None or q== None:
                return False
            return p.val== q.val and helper(p.left, q.right) and helper(p.right, q.left)
        return helper(root, root)
        
