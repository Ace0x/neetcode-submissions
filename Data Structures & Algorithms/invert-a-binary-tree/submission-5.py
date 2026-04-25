# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [root]
        while len(s) > 0:
            x = s.pop()
            if not x:
                continue
            tmpl = None
            tmpr = None
            if x.left:
                tmpl = x.left
            if x.right:
                tmpr = x.right
            x.right = tmpl
            x.left = tmpr
            s.append(x.right)
            s.append(x.left)
        return root
            

            

                