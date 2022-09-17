class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans= []
        if root is None:
            return ans
        ans+= self.postorderTraversal(root.left)
        ans+= self.postorderTraversal(root.right)
        ans.append(root.val)
        return ans
