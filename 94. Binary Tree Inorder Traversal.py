class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root != None:
            ans += self.inorderTraversal(root.left)
            ans.append(root.val)
            ans += self.inorderTraversal(root.right)
        return ans
