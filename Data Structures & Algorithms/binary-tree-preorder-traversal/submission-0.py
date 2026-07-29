# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def solve(node):
            if node==None:
                return
            res.append(node.val)
            solve(node.left)
            
            solve(node.right)
        solve(root)
        return res
        