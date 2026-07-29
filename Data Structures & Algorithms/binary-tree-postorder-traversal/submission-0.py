# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def solve(node):
            if node==None:
                return
            solve(node.left)
            solve(node.right)
            res.append(node.val)
        solve(root)
        return res
        
        