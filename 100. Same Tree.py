class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        return (p.val== q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
