class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.res += 1
                    covered.update({node, par, node.left, node.right})

        self.res = 0
        covered = {None}
        dfs(root)
        return self.res
