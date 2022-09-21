
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        
        def helper(root):
            if root == None:
                return
            res.append(root.val)
            for i in root.children:
                helper(i)
        helper(root)
        return res
